library(tidyverse)
library(jsonlite)
library(xtable)
library(RVAideMemoire)
library(rcompanion)
library(tseries)

problem_filenames <- Sys.glob("dataset/*_problems_*.json")
problems <- do.call(bind_rows, map(problem_filenames, fromJSON))

procedure_filenames <- Sys.glob("dataset/*_procedures_*.json")
procedures <- do.call(bind_rows, map(procedure_filenames, fromJSON))

configuration_labels <- c(
  "zero-shot" = "Zero-shot",
  "few-shot" = "Few-shot (default)",
  "few-shot-no-restrictions" = "Few-shot (alternative prompt)",
  "no-punctuation" = "No punctuation",
  "no-punctuation-extended-dataset" = "No punctuation (works without punctuation only)",
  "no-translation" = "No translation",
  "no-procedures" = "No procedures",
  "with-numerical-answers" = "Numerical solutions provided"
)

titles_to_pinyin <- c(
  "九章算術" = "Jiuzhang suanshu",
  "五曹算經" = "Wucao suanjing",
  "緝古算經" = "Jigu suanjing",
  "孫子算經" = "Sunzi suanjing",
  "海島算經" = "Haidao suanjing",
  "夏侯陽算經" = "Xiaohou Yang suanjing",
  "張邱建算經"  = "Zhang Qiujian suanjing"
)

title_translations <- c(
  "九章算術" = "Computational Procedures of Nine Categories",
  "五曹算經" = "Computational Treatise of Five Departments",
  "緝古算經" = "Computational Treatise on the Continuation [of Tradition] of Ancient [authors]",
  "孫子算經" = "Computational Treatise of Master Sun",
  "海島算經" = "Computational Treatise [Beginning with a Problem about a] Sea Island",
  "夏侯陽算經" = "Computational Treatise of Xiaohou Yang",
  "張邱建算經"  = "Computational Treatise of Zhang Qiujian"
)

title_dating <- c(
  "九章算術" = "\\makecell{early\\\\1st century}",
  "海島算經" = "ca 263",
  "五曹算經" = "after 386",
  "孫子算經" = "ca 400",
  "張邱建算經"  = "ca 450",
  "緝古算經" = "ca 600",
  "夏侯陽算經" = "763-779"
)

main_results <- read_csv("batch_outputs/20250124_200738/statistics.csv")
main_results <- main_results %>%
  mutate(title = str_split_i(problem_id, "_", 1),
         juan = str_split_i(problem_id, "_", 2),
         configuration = factor(configuration, levels = names(configuration_labels)))

error_analysis <- read_csv("error_analysis/error_analysis.csv")

comment_alignments <- read_delim("batch_outputs/20250124_200738/comment_alignments.csv",
                               escape_double = T)

rownames(problems) <- problems$id
problems <- problems %>% mutate(answer_structured = coalesce(answer_structured, answer_structured_manual))
problems %>%
  mutate(num_unknowns = map_int(answer_structured,
                            ~ sum(map_lgl(.x, function(y) length(y) == 2)))) -> problems

rownames(procedures) <- procedures$id

procedures <- procedures %>%
  mutate(complete_text = if_else(is.na(referenced_procedure),
                                 text,
                                 paste0(text, procedures[referenced_procedure,]$text)
  ))

punctuated_titles <- main_results %>% filter(configuration != "no-punctuation-extended-dataset") %>%
  pull(title) %>% unique()

problems %>%
  group_by(source_title) %>%
  summarise(num_juan = n_distinct(source_juan),
            num_problems = n()) %>%
  arrange(match(source_title, names(title_dating))) %>%
  mutate(has_punctuation = if_else(source_title %in% punctuated_titles, "x", ""), 
         dating = title_dating[source_title],
         source_title = paste0("\\emph{", titles_to_pinyin[source_title], "}", source_title, " (``", title_translations[source_title], "'')")) %>%
  relocate(dating, .after = source_title) %>%
  xtable() %>%
  print(only.contents = T,
        include.colnames = F,
        include.rownames = F,
        hline.after = NULL,
        sanitize.text.function = function(x) x,
        file = "table_content_summary.tex")

max(problems$num_unknowns)
mean(problems$num_unknowns)
sd(problems$num_unknowns)

problems %>%
  group_by(source_title) %>%
  summarise(mean_num_unknowns = mean(num_unknowns),
            mean_question_length = mean(str_length(question)))

min(str_length(procedures$complete_text))
max(str_length(procedures$complete_text))
mean(str_length(procedures$complete_text))
sd(str_length(procedures$complete_text))
procedures %>%
  filter(str_length(text) < 10)

complete_dataset_mean_accuracy_significance <- cochran.qtest(passed ~ configuration | problem_id_run,
              data = main_results %>%
                filter(configuration != "no-punctuation-extended-dataset") %>%
                mutate(problem_id_run = paste(problem_id, run, sep = "#")),
              alpha = 0.05 / (2 * (length(punctuated_titles) + 1)))
complete_dataset_mean_accuracy_significance
complete_dataset_mean_accuracy_best_index <- which.max(complete_dataset_mean_accuracy_significance$estimate)

complete_dataset_best_of_five_significance <- cochran.qtest(passed ~ configuration | problem_id,
                                                            data = main_results %>%
                                                              filter(configuration != "no-punctuation-extended-dataset") %>%
                                                              group_by(configuration, problem_id) %>%
                                                              summarise(passed = any(passed)),
                                                            alpha = 0.05 / (2 * (length(punctuated_titles) + 1)))
complete_dataset_best_of_five_significance
complete_dataset_best_of_five_best_index <- which.max(complete_dataset_best_of_five_significance$estimate)

by_title_mean_accuracy_significance = map(punctuated_titles,
                            function(x) {
                              cochran.qtest(passed ~ configuration | problem_id_run,
                                            data = main_results %>%
                                              filter(configuration != "no-punctuation-extended-dataset") %>%
                                              filter(title == x) %>%
                                              mutate(problem_id_run = paste(problem_id, run, sep = "#")),
                                            alpha = 0.05 / (2 * (length(punctuated_titles) + 1)))
                            })
names(by_title_mean_accuracy_significance) <- punctuated_titles
by_title_mean_accuracy_best_index <- map_int(by_title_mean_accuracy_significance,
                                             ~ which.max(.x$estimate))

by_title_best_of_five_significance = map(punctuated_titles,
                                          function(x) {
                                            cochran.qtest(passed ~ configuration | problem_id,
                                                          data = main_results %>%
                                                            filter(configuration != "no-punctuation-extended-dataset") %>%
                                                            filter(title == x) %>%
                                                            group_by(configuration, problem_id) %>%
                                                            summarise(passed = any(passed)),
                                                          alpha = 0.05 / (2 * (length(punctuated_titles) + 1)))
                                          })
names(by_title_best_of_five_significance) <- punctuated_titles
by_title_best_of_five_best_index <- map_int(by_title_best_of_five_significance,
                                             ~ which.max(.x$estimate))

main_results %>%
  filter(configuration != "no-punctuation-extended-dataset") %>%
  group_by(configuration, problem_id) %>%
  summarise(mean_accuracy = sum(passed) / n(), best_of_five = any(passed)) %>%
  mutate(complete_dataset_mean_accuracy = 100 * mean(mean_accuracy),
         complete_dataset_best_of_five = 100 * mean(best_of_five)) %>%
  mutate(title = str_split_i(problem_id, "_", 1)) %>%
  group_by(configuration, title) %>%
  summarise(mean_accuracy = 100 * mean(mean_accuracy),
            mean_best_of_five = 100 * mean(best_of_five),
            complete_dataset_mean_accuracy = first(complete_dataset_mean_accuracy), 
            complete_dataset_best_of_five = first(complete_dataset_best_of_five)) %>%
  mutate(across(where(is.numeric), ~ formatC(.x, format = "f", digits = 1))) %>%
  select(!ends_with("best")) %>%
  pivot_wider(names_from = title, values_from = c(mean_accuracy, mean_best_of_five)) %>%
  relocate(configuration, complete_dataset_mean_accuracy, complete_dataset_best_of_five,
           mean_accuracy_九章算術, mean_best_of_five_九章算術,
           mean_accuracy_海島算經, mean_best_of_five_海島算經,
           mean_accuracy_五曹算經, mean_best_of_five_五曹算經,
           mean_accuracy_孫子算經, mean_best_of_five_孫子算經,
           mean_accuracy_緝古算經, mean_best_of_five_緝古算經) %>%
  mutate(configuration = configuration_labels[configuration]) %>%
  arrange(match(configuration, configuration_labels)) %>%
  xtable() %>%
  print(only.contents = T,
        include.colnames = F,
        include.rownames = F,
        hline.after = NULL,
        sanitize.text.function = function(x) x,
        file = "table_main_results.tex")

main_results %>%
  filter(configuration == "no-punctuation-extended-dataset") %>%
  group_by(problem_id) %>%
  summarise(mean_accuracy = sum(passed) / n(), best_of_five = any(passed)) %>%
  mutate(complete_dataset_mean_accuracy = 100 * mean(mean_accuracy),
         complete_dataset_best_of_five = 100 * mean(best_of_five)) %>%
  mutate(title = str_split_i(problem_id, "_", 1)) %>%
  group_by(title) %>%
  summarise(mean_accuracy = 100 * mean(mean_accuracy),
            mean_best_of_five = 100 * mean(best_of_five),
            complete_dataset_mean_accuracy = first(complete_dataset_mean_accuracy), 
            complete_dataset_best_of_five = first(complete_dataset_best_of_five)) %>%
  mutate(across(where(is.numeric), ~ formatC(.x, format = "f", digits = 1))) %>%
  pivot_wider(names_from = title, values_from = c(mean_accuracy, mean_best_of_five)) %>%
  relocate(complete_dataset_mean_accuracy, complete_dataset_best_of_five,
           mean_accuracy_夏侯陽算經, mean_best_of_five_夏侯陽算經,
           mean_accuracy_張邱建算經, mean_best_of_five_張邱建算經) %>%
  xtable() %>%
  print(only.contents = T,
        include.colnames = F,
        include.rownames = F,
        hline.after = NULL,
        sanitize.text.function = function(x) x,
        file = "table_no_punctuation_results.tex")

punctuated_title_juans <- 
  main_results %>% filter(configuration != "no-punctuation-extended-dataset") %>%
  mutate(x = paste(title, juan, sep = "#")) %>%
  pull(x) %>%
  unique()

by_juan_mean_accuracy_significance = map(punctuated_title_juans,
                                         function(x) {
                                           cochran.qtest(passed ~ configuration | problem_id_run,
                                                         data = main_results %>%
                                                           filter(configuration != "no-punctuation-extended-dataset") %>%
                                                           filter(title == str_split_i(x, "#", 1) &
                                                                    juan == str_split_i(x, "#", 2)) %>%
                                                           mutate(problem_id_run = paste(problem_id, run, sep = "#")),
                                                         alpha = 0.05 / (2 * length(punctuated_title_juans)))
                                         })
names(by_juan_mean_accuracy_significance) <- punctuated_title_juans
by_juan_mean_accuracy_best_index <- map_int(by_juan_mean_accuracy_significance,
                                            ~ which.max(.x$estimate))

by_juan_best_of_five_significance = map(punctuated_title_juans,
                                        function(x) {
                                          cochran.qtest(passed ~ configuration | problem_id,
                                                        data = main_results %>%
                                                          filter(configuration != "no-punctuation-extended-dataset") %>%
                                                          filter(title == str_split_i(x, "#", 1) &
                                                                   juan == str_split_i(x, "#", 2)) %>%
                                                          group_by(configuration, problem_id) %>%
                                                          summarise(passed = any(passed)),
                                                        alpha = 0.05 / (2 * length(punctuated_title_juans)))
                                        })
names(by_juan_best_of_five_significance) <- punctuated_title_juans
by_juan_best_of_five_best_index <- map_int(by_juan_best_of_five_significance,
                                           ~ which.max(.x$estimate))

main_results_by_juan <- main_results %>%
  filter(configuration != "no-punctuation-extended-dataset") %>%
  group_by(configuration, title, juan, problem_id) %>%
  summarise(mean_accuracy = mean(passed), best_of_five = any(passed)) %>%
  group_by(configuration, title, juan) %>%
  summarise(mean_accuracy = 100 * mean(mean_accuracy),
            mean_best_of_five = 100 * mean(best_of_five),
            num_problems = n()) %>%
  pivot_wider(names_from = configuration, values_from = c(mean_accuracy, mean_best_of_five)) %>%
  mutate(title_rles = rle(title)$lengths,
         title = if_else(duplicated(title),
                         "",
                         paste0(if_else(title_rles > 1, paste0("\\multirow{", title_rles, "}{*}{"), ""),
                                "\\makecell{\\emph{",
                                str_replace_all(titles_to_pinyin[title], fixed(" "), "}\\\\\\emph{"),
                                "}}",
                                if_else(title_rles > 1, "}", ""))))


main_results_by_juan %>%
  select(!title_rles) %>%
  relocate(title, juan, num_problems,
           `mean_accuracy_zero-shot`, `mean_best_of_five_zero-shot`,
           `mean_accuracy_few-shot`, `mean_best_of_five_few-shot`,
           `mean_accuracy_few-shot-no-restrictions`, `mean_best_of_five_few-shot-no-restrictions`,
           `mean_accuracy_no-punctuation`, `mean_best_of_five_no-punctuation`,
           `mean_accuracy_no-translation`, `mean_best_of_five_no-translation`,
           `mean_accuracy_no-procedures`, `mean_best_of_five_no-procedures`,
           `mean_accuracy_with-numerical-answers`, `mean_best_of_five_with-numerical-answers`) %>%
  xtable() %>%
  print(only.contents = T,
        include.colnames = F,
        include.rownames = F,
        hline.after = (which(main_results_by_juan$title != "") - 1)[-1],
        sanitize.text.function = function(x) x,
        file = "table_per_juan_results.tex")


# runs test

main_results %>%
  filter(configuration == "few-shot") %>%
  group_by(title, juan, problem_id) %>%
  summarise(best_of_five = any(passed)) %>%
  mutate(title_juan = paste0(title, juan),
         problem_index = as.integer(str_split_i(problem_id, "_", 3))) %>%
  ggplot(aes(x = title_juan, y = problem_index, fill = best_of_five)) +
  geom_tile()

main_results %>%
  filter(configuration == "few-shot") %>%
  group_by(title, juan, problem_id) %>%
  summarise(best_of_five = any(passed)) %>%
  group_by(title, juan) %>%
  summarise(p_value = runs.test(factor(best_of_five, levels = c(T, F)))$p.value) %>%
  ungroup() %>%
  mutate(p_value = p.adjust(p_value, method = "holm")) %>%
  count(p_value < 0.05)

# relation between text length and outcome
problems %>%
  left_join(procedures, by = join_by(procedure_id == id)) %>%
  mutate(total_str_length = str_length(question) + str_length(answer) + str_length(complete_text)) %>%
  group_by(source_title.x) %>%
  summarise(mean_length = mean(total_str_length),
            mean_num_unknowns = mean(num_unknowns))

passed_by_total_str_length_num_unknowns <- glm(passed ~ total_str_length + num_unknowns, data = main_results %>%
                                                 filter(configuration == "few-shot") %>%
                                                 left_join(problems, by = join_by(problem_id == id)) %>%
                                                 left_join(procedures, by = join_by(procedure_id == id)) %>%
                                                 mutate(total_str_length = str_length(question) + str_length(answer) + str_length(complete_text)),
                                               family = binomial)
summary(passed_by_total_str_length_num_unknowns)

passed_by_num_unknowns <- glm(passed ~ num_unknowns, data = main_results %>%
                                filter(configuration == "few-shot") %>%
                                left_join(problems, by = join_by(problem_id == id)),
                              family = binomial)
summary(passed_by_num_unknowns)

# error analysis
global_error_types <- c(
  "misunderstood question",
  "misunderstood procedure",
  "misunderstood procedure (inference required)"
)

error_analysis %>%
  count(error_type) %>%
  mutate(is_global_error = error_type %in% global_error_types) %>%
  arrange(desc(is_global_error), desc(n)) %>%
  mutate(is_global_error = if_else(is_global_error, "global", "localized")) %>%
  group_by(is_global_error) %>%
  mutate(is_global_error = if_else(duplicated(is_global_error),
                                   "",
                                   paste0(paste0("\\multirow{", n(), "}{*}{",
                                                 is_global_error, "}")))) %>%
  relocate(is_global_error) %>%
  xtable() %>%
  print(only.contents = T,
        include.colnames = F,
        include.rownames = F,
        hline.after = length(global_error_types),
        sanitize.text.function = function(x) x,
        file = "table_error_types.tex")

# comment alignments
comment_alignments %>%
  group_by(configuration) %>%
  summarise(aligned_proportion = mean(aligned))

comment_alignments %>%
  filter(configuration == "few-shot") %>%
  filter(aligned) %>%
  group_by(problem_id) %>%
  mutate(aligned_chars = sum(str_length(comment))) %>%
  slice_max(tibble(aligned_chars, run), n = 1) %>%
  ungroup() %>%
  filter(grepl(fixed(" \\* "), code_lines)) %>%
  mutate(has_cheng = grepl("乘", comment),
         has_bei = grepl("倍", comment),
         has_ming = grepl("命", comment),
         has_n_zhi = grepl("[一二三四五六七八九十]+之", comment),
         is_conversion = grepl("[Cc]onvert", code_lines)) %>%
  mutate(title = str_split_i(problem_id, "_", 1)) %>%
  group_by(title) %>%
  summarise(cheng = sum(has_cheng),
            n_zhi = sum(has_n_zhi),
            bei = sum(has_bei),
            ming = sum(has_ming),
            conversion = sum(is_conversion),
            other = sum(!has_cheng & !has_ming & !has_bei & !has_n_zhi & !is_conversion),
            total = n()) %>%
  mutate(across(where(is.numeric), ~ paste0(.x, " (", round(100 * .x / total), "\\%)"))) %>%
  mutate(title = paste0("\\emph{", titles_to_pinyin[title], "}")) %>%
  select(!total) %>%
  xtable() %>%
  print(only.contents = T,
        include.colnames = F,
        include.rownames = F,
        hline.after = NULL,
        sanitize.text.function = function(x) x,
        file = "table_multiplications.tex")
