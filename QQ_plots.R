Link <- read.csv(file.choose()) # Choose the csv file from the dialog box
# Noraml Fitting QQ Plot
data = Link$Total #Total/First/Second/Third/Fourth/Fifth/Sixth
qqnorm(data)
qqline(data)
	## OR
data = Link$Total #Total/First/Second/Third/Fourth/Fifth/Sixth
qqPlot(data, distribution = "norm", xlab="Theoretical Quantiles", ylab="Sample Quantiles")
title(main = "Lognormal Q-Q plot")	

# Log_noraml Fitting QQ Plot
library("car")
data = Link$Total #Total/First/Second/Third/Fourth/Fifth/Sixth
qqPlot(data, distribution = "lnorm", xlab="Theoretical Quantiles", ylab="Sample Quantiles")
title(main = "Lognormal Q-Q plot")