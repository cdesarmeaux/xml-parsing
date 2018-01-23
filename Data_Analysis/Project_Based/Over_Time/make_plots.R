require(sqldf)
library(doBy)
library(ggplot2)
library(plyr)
library(scales)
pom = read.csv("rq.csv")
m1_1 = sqldf("select proj, phase from pom where month > 0 and month < 11")
m1_2 = sqldf("select proj, phase, count(phase) as count from m1_1 group by proj,phase")
m1_3 = sqldf("select proj, phase, count, sum(count) as sums from m1_2 group by proj")
m1_4 = sqldf("select m1_2.proj, m1_2.phase, m1_2.count, m1_3.sums from m1_2, m1_3 where m1_2.proj = m1_3.proj")
m1_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m1_4")

m2_1 = sqldf("select proj, phase from pom where month > 10 and month < 21")
m2_2 = sqldf("select proj, phase, count(phase) as count from m2_1 group by proj,phase")
m2_3 = sqldf("select proj, phase, count, sum(count) as sums from m2_2 group by proj")
m2_4 = sqldf("select m2_2.proj, m2_2.phase, m2_2.count, m2_3.sums from m2_2, m2_3 where m2_2.proj = m2_3.proj")
m2_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m2_4")

m3_1 = sqldf("select proj, phase from pom where month > 20 and month < 31")
m3_2 = sqldf("select proj, phase, count(phase) as count from m3_1 group by proj,phase")
m3_3 = sqldf("select proj, phase, count, sum(count) as sums from m3_2 group by proj")
m3_4 = sqldf("select m3_2.proj, m3_2.phase, m3_2.count, m3_3.sums from m3_2, m3_3 where m3_2.proj = m3_3.proj")
m3_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m3_4")

m4_1 = sqldf("select proj, phase from pom where month > 30 and month < 41")
m4_2 = sqldf("select proj, phase, count(phase) as count from m4_1 group by proj,phase")
m4_3 = sqldf("select proj, phase, count, sum(count) as sums from m4_2 group by proj")
m4_4 = sqldf("select m4_2.proj, m4_2.phase, m4_2.count, m4_3.sums from m4_2, m4_3 where m4_2.proj = m4_3.proj")
m4_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m4_4")

m5_1 = sqldf("select proj, phase from pom where month > 40 and month < 51")
m5_2 = sqldf("select proj, phase, count(phase) as count from m5_1 group by proj,phase")
m5_3 = sqldf("select proj, phase, count, sum(count) as sums from m5_2 group by proj")
m5_4 = sqldf("select m5_2.proj, m5_2.phase, m5_2.count, m5_3.sums from m5_2, m5_3 where m5_2.proj = m5_3.proj")
m5_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m5_4")

m6_1 = sqldf("select proj, phase from pom where month > 50 and month < 61")
m6_2 = sqldf("select proj, phase, count(phase) as count from m6_1 group by proj,phase")
m6_3 = sqldf("select proj, phase, count, sum(count) as sums from m6_2 group by proj")
m6_4 = sqldf("select m6_2.proj, m6_2.phase, m6_2.count, m6_3.sums from m6_2, m6_3 where m6_2.proj = m6_3.proj")
m6_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m6_4")

m7_1 = sqldf("select proj, phase from pom where month > 60 and month < 71")
m7_2 = sqldf("select proj, phase, count(phase) as count from m7_1 group by proj,phase")
m7_3 = sqldf("select proj, phase, count, sum(count) as sums from m7_2 group by proj")
m7_4 = sqldf("select m7_2.proj, m7_2.phase, m7_2.count, m7_3.sums from m7_2, m7_3 where m7_2.proj = m7_3.proj")
m7_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m7_4")

m8_1 = sqldf("select proj, phase from pom where month > 70 and month < 81")
m8_2 = sqldf("select proj, phase, count(phase) as count from m8_1 group by proj,phase")
m8_3 = sqldf("select proj, phase, count, sum(count) as sums from m8_2 group by proj")
m8_4 = sqldf("select m8_2.proj, m8_2.phase, m8_2.count, m8_3.sums from m8_2, m8_3 where m8_2.proj = m8_3.proj")
m8_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m8_4")

m9_1 = sqldf("select proj, phase from pom where month > 80 and month < 91")
m9_2 = sqldf("select proj, phase, count(phase) as count from m9_1 group by proj,phase")
m9_3 = sqldf("select proj, phase, count, sum(count) as sums from m9_2 group by proj")
m9_4 = sqldf("select m9_2.proj, m9_2.phase, m9_2.count, m9_3.sums from m9_2, m9_3 where m9_2.proj = m9_3.proj")
m9_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m9_4")

m10_1 = sqldf("select proj, phase from pom where month > 90 and month < 101")
m10_2 = sqldf("select proj, phase, count(phase) as count from m10_1 group by proj,phase")
m10_3 = sqldf("select proj, phase, count, sum(count) as sums from m10_2 group by proj")
m10_4 = sqldf("select m10_2.proj, m10_2.phase, m10_2.count, m10_3.sums from m10_2, m10_3 where m10_2.proj = m10_3.proj")
m10_5 = sqldf("select proj, phase, (CAST(count AS float)/CAST(sums AS float)) as perc from m10_4")

validateMed1 = sqldf("select * from m1_5 where phase = 'validate'")
validateMed2 = sqldf("select * from m2_5 where phase = 'validate'")
validateMed3 = sqldf("select * from m3_5 where phase = 'validate'")
validateMed4 = sqldf("select * from m4_5 where phase = 'validate'")
validateMed5 = sqldf("select * from m5_5 where phase = 'validate'")
validateMed6 = sqldf("select * from m6_5 where phase = 'validate'")
validateMed7 = sqldf("select * from m7_5 where phase = 'validate'")
validateMed8 = sqldf("select * from m8_5 where phase = 'validate'")
validateMed9 = sqldf("select * from m9_5 where phase = 'validate'")
validateMed10 = sqldf("select * from m10_5 where phase = 'validate'")
compileMed1 = sqldf("select * from m1_5 where phase = 'compile'")
compileMed2 = sqldf("select * from m2_5 where phase = 'compile'")
compileMed3 = sqldf("select * from m3_5 where phase = 'compile'")
compileMed4 = sqldf("select * from m4_5 where phase = 'compile'")
compileMed5 = sqldf("select * from m5_5 where phase = 'compile'")
compileMed6 = sqldf("select * from m6_5 where phase = 'compile'")
compileMed7 = sqldf("select * from m7_5 where phase = 'compile'")
compileMed8 = sqldf("select * from m8_5 where phase = 'compile'")
compileMed9 = sqldf("select * from m9_5 where phase = 'compile'")
compileMed10 = sqldf("select * from m10_5 where phase = 'compile'")
testMed1 = sqldf("select * from m1_5 where phase = 'test'")
testMed2 = sqldf("select * from m2_5 where phase = 'test'")
testMed3 = sqldf("select * from m3_5 where phase = 'test'")
testMed4 = sqldf("select * from m4_5 where phase = 'test'")
testMed5 = sqldf("select * from m5_5 where phase = 'test'")
testMed6 = sqldf("select * from m6_5 where phase = 'test'")
testMed7 = sqldf("select * from m7_5 where phase = 'test'")
testMed8 = sqldf("select * from m8_5 where phase = 'test'")
testMed9 = sqldf("select * from m9_5 where phase = 'test'")
testMed10 = sqldf("select * from m10_5 where phase = 'test'")
packagingMed1 = sqldf("select * from m1_5 where phase = 'packaging'")
packagingMed2 = sqldf("select * from m2_5 where phase = 'packaging'")
packagingMed3 = sqldf("select * from m3_5 where phase = 'packaging'")
packagingMed4 = sqldf("select * from m4_5 where phase = 'packaging'")
packagingMed5 = sqldf("select * from m5_5 where phase = 'packaging'")
packagingMed6 = sqldf("select * from m6_5 where phase = 'packaging'")
packagingMed7 = sqldf("select * from m7_5 where phase = 'packaging'")
packagingMed8 = sqldf("select * from m8_5 where phase = 'packaging'")
packagingMed9 = sqldf("select * from m9_5 where phase = 'packaging'")
packagingMed10 = sqldf("select * from m10_5 where phase = 'packaging'")
installMed1 = sqldf("select * from m1_5 where phase = 'install'")
installMed2 = sqldf("select * from m2_5 where phase = 'install'")
installMed3 = sqldf("select * from m3_5 where phase = 'install'")
installMed4 = sqldf("select * from m4_5 where phase = 'install'")
installMed5 = sqldf("select * from m5_5 where phase = 'install'")
installMed6 = sqldf("select * from m6_5 where phase = 'install'")
installMed7 = sqldf("select * from m7_5 where phase = 'install'")
installMed8 = sqldf("select * from m8_5 where phase = 'install'")
installMed9 = sqldf("select * from m9_5 where phase = 'install'")
installMed10 = sqldf("select * from m10_5 where phase = 'install'")
deployMed1 = sqldf("select * from m1_5 where phase = 'deploy'")
deployMed2 = sqldf("select * from m2_5 where phase = 'deploy'")
deployMed3 = sqldf("select * from m3_5 where phase = 'deploy'")
deployMed4 = sqldf("select * from m4_5 where phase = 'deploy'")
deployMed5 = sqldf("select * from m5_5 where phase = 'deploy'")
deployMed6 = sqldf("select * from m6_5 where phase = 'deploy'")
deployMed7 = sqldf("select * from m7_5 where phase = 'deploy'")
deployMed8 = sqldf("select * from m8_5 where phase = 'deploy'")
deployMed9 = sqldf("select * from m9_5 where phase = 'deploy'")
deployMed10 = sqldf("select * from m10_5 where phase = 'deploy'")
validateMean1 = c(1, 'validate', median(validateMed1$perc), quantile(validateMed1$perc)[2], quantile(validateMed1$perc)[4], nrow(validateMed1))
validateMean2 = c(2, 'validate', median(validateMed2$perc), quantile(validateMed2$perc)[2], quantile(validateMed2$perc)[4], nrow(validateMed2))
validateMean3 = c(3, 'validate', median(validateMed3$perc), quantile(validateMed3$perc)[2], quantile(validateMed3$perc)[4], nrow(validateMed3))
validateMean4 = c(4, 'validate', median(validateMed4$perc), quantile(validateMed4$perc)[2], quantile(validateMed4$perc)[4], nrow(validateMed4))
validateMean5 = c(5, 'validate', median(validateMed5$perc), quantile(validateMed5$perc)[2], quantile(validateMed5$perc)[4], nrow(validateMed5))
validateMean6 = c(6, 'validate', median(validateMed6$perc), quantile(validateMed6$perc)[2], quantile(validateMed6$perc)[4], nrow(validateMed6))
validateMean7 = c(7, 'validate', median(validateMed7$perc), quantile(validateMed7$perc)[2], quantile(validateMed7$perc)[4], nrow(validateMed7))
validateMean8 = c(8, 'validate', median(validateMed8$perc), quantile(validateMed8$perc)[2], quantile(validateMed8$perc)[4], nrow(validateMed8))
validateMean9 = c(9, 'validate', median(validateMed9$perc), quantile(validateMed9$perc)[2], quantile(validateMed9$perc)[4], nrow(validateMed9))
validateMean10 = c(10, 'validate', median(validateMed10$perc), quantile(validateMed10$perc)[2], quantile(validateMed10$perc)[4], nrow(validateMed10))
compileMean1 = c(1, 'compile', median(compileMed1$perc), quantile(compileMed1$perc)[2], quantile(compileMed1$perc)[4], nrow(compileMed1))
compileMean2 = c(2, 'compile', median(compileMed2$perc), quantile(compileMed2$perc)[2], quantile(compileMed2$perc)[4], nrow(compileMed2))
compileMean3 = c(3, 'compile', median(compileMed3$perc), quantile(compileMed3$perc)[2], quantile(compileMed3$perc)[4], nrow(compileMed3))
compileMean4 = c(4, 'compile', median(compileMed4$perc), quantile(compileMed4$perc)[2], quantile(compileMed4$perc)[4], nrow(compileMed4))
compileMean5 = c(5, 'compile', median(compileMed5$perc), quantile(compileMed5$perc)[2], quantile(compileMed5$perc)[4], nrow(compileMed5))
compileMean6 = c(6, 'compile', median(compileMed6$perc), quantile(compileMed6$perc)[2], quantile(compileMed6$perc)[4], nrow(compileMed6))
compileMean7 = c(7, 'compile', median(compileMed7$perc), quantile(compileMed7$perc)[2], quantile(compileMed7$perc)[4], nrow(compileMed7))
compileMean8 = c(8, 'compile', median(compileMed8$perc), quantile(compileMed8$perc)[2], quantile(compileMed8$perc)[4], nrow(compileMed8))
compileMean9 = c(9, 'compile', median(compileMed9$perc), quantile(compileMed9$perc)[2], quantile(compileMed9$perc)[4], nrow(compileMed9))
compileMean10 = c(10, 'compile', median(compileMed10$perc), quantile(compileMed10$perc)[2], quantile(compileMed10$perc)[4], nrow(compileMed10))
testMean1 = c(1, 'test', median(testMed1$perc), quantile(testMed1$perc)[2], quantile(testMed1$perc)[4], nrow(testMed1))
testMean2 = c(2, 'test', median(testMed2$perc), quantile(testMed2$perc)[2], quantile(testMed2$perc)[4], nrow(testMed2))
testMean3 = c(3, 'test', median(testMed3$perc), quantile(testMed3$perc)[2], quantile(testMed3$perc)[4], nrow(testMed3))
testMean4 = c(4, 'test', median(testMed4$perc), quantile(testMed4$perc)[2], quantile(testMed4$perc)[4], nrow(testMed4))
testMean5 = c(5, 'test', median(testMed5$perc), quantile(testMed5$perc)[2], quantile(testMed5$perc)[4], nrow(testMed5))
testMean6 = c(6, 'test', median(testMed6$perc), quantile(testMed6$perc)[2], quantile(testMed6$perc)[4], nrow(testMed6))
testMean7 = c(7, 'test', median(testMed7$perc), quantile(testMed7$perc)[2], quantile(testMed7$perc)[4], nrow(testMed7))
testMean8 = c(8, 'test', median(testMed8$perc), quantile(testMed8$perc)[2], quantile(testMed8$perc)[4], nrow(testMed8))
testMean9 = c(9, 'test', median(testMed9$perc), quantile(testMed9$perc)[2], quantile(testMed9$perc)[4], nrow(testMed9))
testMean10 = c(10, 'test', median(testMed10$perc), quantile(testMed10$perc)[2], quantile(testMed10$perc)[4], nrow(testMed10))
packagingMean1 = c(1, 'packaging', median(packagingMed1$perc), quantile(packagingMed1$perc)[2], quantile(packagingMed1$perc)[4], nrow(packagingMed1))
packagingMean2 = c(2, 'packaging', median(packagingMed2$perc), quantile(packagingMed2$perc)[2], quantile(packagingMed2$perc)[4], nrow(packagingMed2))
packagingMean3 = c(3, 'packaging', median(packagingMed3$perc), quantile(packagingMed3$perc)[2], quantile(packagingMed3$perc)[4], nrow(packagingMed3))
packagingMean4 = c(4, 'packaging', median(packagingMed4$perc), quantile(packagingMed4$perc)[2], quantile(packagingMed4$perc)[4], nrow(packagingMed4))
packagingMean5 = c(5, 'packaging', median(packagingMed5$perc), quantile(packagingMed5$perc)[2], quantile(packagingMed5$perc)[4], nrow(packagingMed5))
packagingMean6 = c(6, 'packaging', median(packagingMed6$perc), quantile(packagingMed6$perc)[2], quantile(packagingMed6$perc)[4], nrow(packagingMed6))
packagingMean7 = c(7, 'packaging', median(packagingMed7$perc), quantile(packagingMed7$perc)[2], quantile(packagingMed7$perc)[4], nrow(packagingMed7))
packagingMean8 = c(8, 'packaging', median(packagingMed8$perc), quantile(packagingMed8$perc)[2], quantile(packagingMed8$perc)[4], nrow(packagingMed8))
packagingMean9 = c(9, 'packaging', median(packagingMed9$perc), quantile(packagingMed9$perc)[2], quantile(packagingMed9$perc)[4], nrow(packagingMed9))
packagingMean10 = c(10, 'packaging', median(packagingMed10$perc), quantile(packagingMed10$perc)[2], quantile(packagingMed10$perc)[4], nrow(packagingMed10))
installMean1 = c(1, 'install', median(installMed1$perc), quantile(installMed1$perc)[2], quantile(installMed1$perc)[4], nrow(installMed1))
installMean2 = c(2, 'install', median(installMed2$perc), quantile(installMed2$perc)[2], quantile(installMed2$perc)[4], nrow(installMed2))
installMean3 = c(3, 'install', median(installMed3$perc), quantile(installMed3$perc)[2], quantile(installMed3$perc)[4], nrow(installMed3))
installMean4 = c(4, 'install', median(installMed4$perc), quantile(installMed4$perc)[2], quantile(installMed4$perc)[4], nrow(installMed4))
installMean5 = c(5, 'install', median(installMed5$perc), quantile(installMed5$perc)[2], quantile(installMed5$perc)[4], nrow(installMed5))
installMean6 = c(6, 'install', median(installMed6$perc), quantile(installMed6$perc)[2], quantile(installMed6$perc)[4], nrow(installMed6))
installMean7 = c(7, 'install', median(installMed7$perc), quantile(installMed7$perc)[2], quantile(installMed7$perc)[4], nrow(installMed7))
installMean8 = c(8, 'install', median(installMed8$perc), quantile(installMed8$perc)[2], quantile(installMed8$perc)[4], nrow(installMed8))
installMean9 = c(9, 'install', median(installMed9$perc), quantile(installMed9$perc)[2], quantile(installMed9$perc)[4], nrow(installMed9))
installMean10 = c(10, 'install', median(installMed10$perc), quantile(installMed10$perc)[2], quantile(installMed10$perc)[4], nrow(installMed10))
deployMean1 = c(1, 'deploy', median(deployMed1$perc), quantile(deployMed1$perc)[2], quantile(deployMed1$perc)[4], nrow(deployMed1))
deployMean2 = c(2, 'deploy', median(deployMed2$perc), quantile(deployMed2$perc)[2], quantile(deployMed2$perc)[4], nrow(deployMed2))
deployMean3 = c(3, 'deploy', median(deployMed3$perc), quantile(deployMed3$perc)[2], quantile(deployMed3$perc)[4], nrow(deployMed3))
deployMean4 = c(4, 'deploy', median(deployMed4$perc), quantile(deployMed4$perc)[2], quantile(deployMed4$perc)[4], nrow(deployMed4))
deployMean5 = c(5, 'deploy', median(deployMed5$perc), quantile(deployMed5$perc)[2], quantile(deployMed5$perc)[4], nrow(deployMed5))
deployMean6 = c(6, 'deploy', median(deployMed6$perc), quantile(deployMed6$perc)[2], quantile(deployMed6$perc)[4], nrow(deployMed6))
deployMean7 = c(7, 'deploy', median(deployMed7$perc), quantile(deployMed7$perc)[2], quantile(deployMed7$perc)[4], nrow(deployMed7))
deployMean8 = c(8, 'deploy', median(deployMed8$perc), quantile(deployMed8$perc)[2], quantile(deployMed8$perc)[4], nrow(deployMed8))
deployMean9 = c(9, 'deploy', median(deployMed9$perc), quantile(deployMed9$perc)[2], quantile(deployMed9$perc)[4], nrow(deployMed9))
deployMean10 = c(10, 'deploy', median(deployMed10$perc), quantile(deployMed10$perc)[2], quantile(deployMed10$perc)[4], nrow(deployMed10))

arr <- array(0, dim=c(10,6))
arr[1,] = validateMean1
arr[2,] = validateMean2
arr[3,] = validateMean3
arr[4,] = validateMean4
arr[5,] = validateMean5
arr[6,] = validateMean6
arr[7,] = validateMean7
arr[8,] = validateMean8
arr[9,] = validateMean9
arr[10,] = validateMean10
write.csv(arr, "data.csv")
validatePlotter = read.csv("data.csv")
validatePlotter = rename(validatePlotter, c("V2"="phase", "V6"="size"))


arr <- array(0, dim=c(10,6))
arr[1,] = compileMean1
arr[2,] = compileMean2
arr[3,] = compileMean3
arr[4,] = compileMean4
arr[5,] = compileMean5
arr[6,] = compileMean6
arr[7,] = compileMean7
arr[8,] = compileMean8
arr[9,] = compileMean9
arr[10,] = compileMean10
write.csv(arr, "data.csv")
compilePlotter = read.csv("data.csv")
compilePlotter = rename(compilePlotter, c("V2"="phase", "V6"="size"))


arr <- array(0, dim=c(10,6))
arr[1,] = testMean1
arr[2,] = testMean2
arr[3,] = testMean3
arr[4,] = testMean4
arr[5,] = testMean5
arr[6,] = testMean6
arr[7,] = testMean7
arr[8,] = testMean8
arr[9,] = testMean9
arr[10,] = testMean10
write.csv(arr, "data.csv")
testPlotter = read.csv("data.csv")
testPlotter = rename(testPlotter, c("V2"="phase", "V6"="size"))



arr <- array(0, dim=c(10,6))
arr[1,] = packagingMean1
arr[2,] = packagingMean2
arr[3,] = packagingMean3
arr[4,] = packagingMean4
arr[5,] = packagingMean5
arr[6,] = packagingMean6
arr[7,] = packagingMean7
arr[8,] = packagingMean8
arr[9,] = packagingMean9
arr[10,] = packagingMean10
write.csv(arr, "data.csv")
packagePlotter = read.csv("data.csv")
packagePlotter = rename(packagePlotter, c("V2"="phase", "V6"="size"))



arr <- array(0, dim=c(10,6))
arr[1,] = installMean1
arr[2,] = installMean2
arr[3,] = installMean3
arr[4,] = installMean4
arr[5,] = installMean5
arr[6,] = installMean6
arr[7,] = installMean7
arr[8,] = installMean8
arr[9,] = installMean9
arr[10,] = installMean10
write.csv(arr, "data.csv")
installPlotter = read.csv("data.csv")
installPlotter = rename(installPlotter, c("V2"="phase", "V6"="size"))



arr <- array(0, dim=c(10,6))
arr[1,] = deployMean1
arr[2,] = deployMean2
arr[3,] = deployMean3
arr[4,] = deployMean4
arr[5,] = deployMean5
arr[6,] = deployMean6
arr[7,] = deployMean7
arr[8,] = deployMean8
arr[9,] = deployMean9
arr[10,] = deployMean10
write.csv(arr, "data.csv")
deployPlotter = read.csv("data.csv")
deployPlotter = rename(deployPlotter, c("V2"="phase", "V6"="size"))



pdf('validate.pdf',  width = 11, height = 8)
ggplot(data=validatePlotter, aes(x=V1, y=V3, group=phase)) + geom_line() + geom_point(aes(size = size)) + theme_bw(base_size = 17) +theme(legend.position = c(.1, .85), legend.key.size = unit(1, "cm")) + scale_size(name ="Projects", breaks = c(1,10,100,1000), limits = c(1, 8230), range = c(2, 24)) + geom_errorbar(aes(ymin=validatePlotter$V4, ymax=validatePlotter$V5), width=.1, linetype = 2) + labs(x = "Commits (x10)") + labs(y = "Percentage of Change") + scale_y_continuous(labels=percent_format(), limits = c(0,1)) + scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9,10))
dev.off()
pdf('compile.pdf', width = 11, height = 8)
ggplot(data=compilePlotter, aes(x=V1, y=V3, group=phase)) + geom_line() + geom_point(aes(size = size)) + theme_bw(base_size=17) + theme(legend.position = "none") + scale_size(name ="Projects", breaks = c(1,10,100,1000), limits = c(1, 8230), range = c(2, 24)) + geom_errorbar(aes(ymin=compilePlotter$V4, ymax=compilePlotter$V5), width=.1, linetype = 2) + labs(x = "Commits (x10)") + labs(y = "Percentage of Change") + scale_y_continuous(labels=percent_format(), limits = c(0,1)) + scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9,10))
dev.off()
pdf('test.pdf', width = 11, height = 8)
ggplot(data=testPlotter, aes(x=V1, y=V3, group=phase)) + geom_line() + geom_point(aes(size = size)) + theme_bw(base_size=17) + theme(legend.position = "none") + scale_size(name ="Projects", breaks = c(1,10,100,1000), limits = c(1, 8230), range = c(2, 24)) + geom_errorbar(aes(ymin=testPlotter$V4, ymax=testPlotter$V5), width=.1, linetype = 2) + labs(x = "Commits (x10)") + labs(y = "Percentage of Change") + scale_y_continuous(labels=percent_format(), limits = c(0,1)) + scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9,10))
dev.off()
pdf('packaging.pdf', width = 11, height = 8)
ggplot(data=packagePlotter, aes(x=V1, y=V3, group=phase)) + geom_line() + geom_point(aes(size = size)) + theme_bw(base_size=17) + theme(legend.position = "none") + scale_size(name ="Projects", breaks = c(1,10,100,1000), limits = c(1, 8230), range = c(2, 24)) + geom_errorbar(aes(ymin=packagePlotter$V4, ymax=packagePlotter$V5), width=.1, linetype = 2) + labs(x = "Commits (x10)") + labs(y = "Percentage of Change") + scale_y_continuous(labels=percent_format(), limits = c(0,1)) + scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9,10))
dev.off()
pdf('install.pdf', width = 11, height = 8)
ggplot(data=installPlotter, aes(x=V1, y=V3, group=phase)) + geom_line() + geom_point(aes(size = size)) + theme_bw(base_size=17) + theme(legend.position = "none") + scale_size(name ="Projects", breaks = c(1,10,100,1000), limits = c(1, 8230), range = c(2, 24)) + geom_errorbar(aes(ymin=installPlotter$V4, ymax=installPlotter$V5), width=.1, linetype = 2) + labs(x = "Commits (x10)") + labs(y = "Percentage of Change") + scale_y_continuous(labels=percent_format(), limits = c(0,1)) + scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9,10))
dev.off()
pdf('deploy.pdf', width = 11, height = 8)
ggplot(data=deployPlotter, aes(x=V1, y=V3, group=phase)) + geom_line() + geom_point(aes(size = size)) + theme_bw(base_size=17) + theme(legend.position = "none") + scale_size(name ="Projects", breaks = c(1,10,100,1000), limits = c(1, 8230), range = c(2, 24)) + geom_errorbar(aes(ymin=deployPlotter$V4, ymax=deployPlotter$V5), width=.1, linetype = 2) + labs(x = "Commits (x10)") + labs(y = "Percentage of Change") + scale_y_continuous(labels=percent_format(), limits = c(0,1)) + scale_x_continuous(breaks = c(1,2,3,4,5,6,7,8,9,10))
dev.off()


