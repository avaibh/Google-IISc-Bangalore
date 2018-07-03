library(fitdistrplus)
library(logspline)

Link <- read.csv(file.choose()) ##  choose file for the total/first/second....sixth distribution

x <- Link$Total ## read the data of choosen file

fit.weibull <- fitdist(x, "weibull")
fit.norm <- fitdist(x, "norm")
fit.lnorm <- fitdist(x, "lnorm")
# fit.norm <- fitdist(x, "norm")
plot(fit.norm)
plot(fit.weibull)
plot(fit.lnorm)

n.sims <- 5e4

## KS Test
ks.test(d, "pnorm", mean=mean(d), sd=sd(d)
ks.test(d, "pweibull", scale=43.2474500, shape=6.4632971)
ks.test(d, "plnorm", meanlog=meanlog(d), sdlog=sdlog(d))


## to run the simulated KS test cdf
stats <- replicate(n.sims, {      
  r <- rweibull(n = length(x)
                , shape= fit.weibull$estimate["shape"]
                , scale = fit.weibull$estimate["scale"]
  )
  as.numeric(ks.test(r
                     , "pweibull"
                     , shape= fit.weibull$estimate["shape"]
                     , scale = fit.weibull$estimate["scale"])$statistic
  )      
})

plot(ecdf(stats), las = 1, main = "KS-test statistic simulation (CDF)", col = "darkorange", lwd = 1.7)
grid()