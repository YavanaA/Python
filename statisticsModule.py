import statistics

Numbers = [3, 4, 4, 6, 3, 54, 5, 6, 8, 4, 34, 545, 45, 334, 43, 3, 43, 3, 32, 22]

mean = statistics.mean(Numbers)  # provide accurate mean compared with the fmean
median = statistics.median(Numbers)
mode = statistics.mode(Numbers)
fmean = statistics.fmean(Numbers)  # new added in python 3.8 and provide some precise not accurate
median_high = statistics.median_high(Numbers)
median_low = statistics.median_low(Numbers)

#  print statement with multiline string, do not forget to use triple quote
print(f""" Given Data = {Numbers} \nMean : {mean} 
Median : {median}
Mode : {mode}
fmean : {fmean}
median_high : {median_high}
median_low : {median_low}""")
