library("dplyr")
library("data.table")

data <- fread('heats_A.csv')
data <- data %>% arrange(time)
data <- data %>% mutate(rank = c(1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8))
data <- data %>% mutate(start = ifelse(rank == 7, 1, ifelse(rank == 5, 2, ifelse(rank == 3, 3,
ifelse(rank == 1, 4, ifelse(rank == 2, 5, ifelse(rank == 4, 6, ifelse(rank == 6, 7, 8))))))))
data <- data %>% mutate(new_heat = c(3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1))
selected <- data %>% filter(heat == 0) %>% arrange(id) %>% select(id, new_heat, start)