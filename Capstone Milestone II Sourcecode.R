#Reading and renaming unfiltered dataset into an R data frame 
RawObesityDataset <- read.csv(file.choose())
Sys.Date()

#Reading and renaming cleaned dataset into an R data frame 
ObesityDataset <- read.csv(file.choose())
Sys.Date()

#Providing basic information on the dataset
str(ObesityDataset)
Sys.Date()

#Selecting variable "Estimate" for quantitative analysis
obesityEST<- (ObesityDataset$ESTIMATE)
Sys.Date()
obesityEST

#Performing descriptive statistical analysis on "Estimate" variable
#Measures of central tendency and dispersion will be calculated
#summary function produces minimum, 1st quartile, median, mean, third quartile, and maximum
summary(obesityEST)
Sys.Date()

#sd()function calculates standard deviation 
sd(obesityEST)
Sys.Date()

#Analysis Date and Time
date()
