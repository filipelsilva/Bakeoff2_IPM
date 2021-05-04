#!/usr/bin/env python3

import os
import subprocess
import matplotlib.pyplot as plt
import math
import statistics

n = [] #preencher com numeros de 1 ate n elementos

accuracy = []
total_times = []
average_time = []
average_time_penalty = []


media_accuracy = statistics.mean(accuracy)
print("Accuracy: "+str(media_accuracy)+"%")
media_total_times = statistics.mean(total_times)
print("Total time: "+str(media_total_times)+"s")
media_average_time = statistics.mean(average_time)
print("Average time: "+str(media_average_time)+"s")
media_average_time_penalty = statistics.mean(average_time_penalty)
print("Average time with penalty: "+str(media_average_time_penalty)+"s")

plt.xticks(n)
plt.xlabel('User')
plt.ylabel('Accuracy')
plt.title("Accuracy: "+str(media_accuracy)+"%", fontsize=12)
plt.plot(n, accuracy, 'o')
plt.savefig('accuracy.png')
plt.clf()

plt.xticks(n)
plt.xlabel('User')
plt.ylabel('Total Time')
plt.title("Total time: "+str(media_total_times)+"s", fontsize=12)
plt.plot(n, total_times, 'o')
plt.savefig('total_times.png')
plt.clf()

plt.xticks(n)
plt.xlabel('User')
plt.ylabel('Average Time')
plt.title("Average time: "+str(media_average_time)+"s", fontsize=12)
plt.plot(n, average_time, 'o')
plt.savefig('average_time.png')
plt.clf()

plt.xticks(n)
plt.xlabel('User')
plt.ylabel('Average Time With Penalty')
plt.title("Average time with penalty: "+str(media_average_time_penalty)+"s", fontsize=12)
plt.plot(n, average_time_penalty, 'o')
plt.savefig('average_time_penalty.png')
plt.clf()
