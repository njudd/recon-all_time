# this script makes the histograms
library(tidyverse)
setwd() #time

base <- read.table("base_time.txt")
MRI1 <- read.table("MRI1_time.txt")
MRI2 <- read.table("MRI2_time.txt")
MRI1.long <- read.table("MRI1.long_time.txt")
MRI2.long <- read.table("MRI2.long_time.txt")

cross_processed <- c(MRI1$V1, MRI2$V1)
long_processed <- c(MRI1.long$V1, MRI2.long$V2)

# ggplot one uses df's

