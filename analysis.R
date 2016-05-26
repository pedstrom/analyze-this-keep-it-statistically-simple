library(readxl)

#read in the data
workbook.file <- "data/SMM Competitor Workbook 5.25.16.xlsx"
ad <- read_excel(workbook.file, sheet="Analytics Dataset")
ml <- read_excel(workbook.file, sheet="Mbrshp Level")
pm <- read_excel(workbook.file, sheet="Pmt Mthd")
sc <- read_excel(workbook.file, sheet="Sales Channel")
o1 <- read_excel(workbook.file, sheet="Offer on 1st Ren Notice")
ei <- read_excel(workbook.file, sheet="Email Indicators")
eo <- read_excel(workbook.file, sheet="EMail Options")
d1 <- read_excel(workbook.file, sheet="Demo_1")
zc <- read_excel(workbook.file, sheet="Zip Code")
kp <- read_excel(workbook.file, sheet="Key people on Membership")
nv <- read_excel(workbook.file, sheet="Num Visits")
cs <- read_excel(workbook.file, sheet="CSIs")
co <- read_excel(workbook.file, sheet="Communication")

