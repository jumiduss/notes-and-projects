import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Controller Reverse Engineering 01.csv",index_col=False)


## Used for analyzing time deltas in section
# new_df = df[df['ID'].str.contains("00000601")]
# two_hun_to_three_hun_df = new_df.loc[846:1221]
# two_to_three_id_df = two_hun_to_three_hun_df['Time Stamp']

# previous_line_id = ''
# previous_time = ''
# f_t_deviation = 0
# for line_id,time in two_to_three_id_df.items():
#     if previous_time == '':
#         previous_time = time
#         f_t_deviation == 510000
#     time_delta = time - previous_time
#     f_t_deviation -= time_delta
#     if f_t_deviation < -250000:
#         f_t_deviation += 510009
    
#     print(f"Time Delta: Lines {line_id}-{previous_line_id} | {time_delta:,} micro-s, Deviation: {f_t_deviation} micro-s, Message: {list(two_hun_to_three_hun_df.loc[line_id])[4:]}")
    
#     previous_line_id = line_id
#     previous_time = time
    
# Used for recording message send times for graph analysis

# set up the figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0,5000)
ax.set_ylim(0,10)

# draw lines
xmin = 0
xmax = 5000
y = 5
height = 1



plt.hlines(y, xmin, xmax)
plt.vlines(xmin, y - height / 2., y + height / 2.)
plt.vlines(xmax, y - height / 2., y + height / 2.)

# draw a point on the line
new_df = df[['ID','Time Stamp']]
index = 0
for row_idx, row_vals in new_df.iterrows():
    
    if row_vals[0] == "00000601":
        color = 'cs'
    elif row_vals[0] == "00000604":
        color = 'bs'
    elif row_vals[0] == "0000060B":
        color = 'ks'
    elif row_vals[0] == "0000060D":
        color = 'gs'
    elif row_vals[0] == "00000610":
        color = 'ms'
    elif row_vals[0] == "00000613":
        color = 'ws'
    elif row_vals[0] == "00000621":
        color = 'rs'
    elif row_vals[0] == "00000681":
        pascolor = 'ys'
    elif row_vals[0] == "000006A1":
        color = 'cs'
    else:
        color = 'ks'
    
    index+=1
    if index == 500:
        break
    
    plt.plot(int(row_vals[1]) / 100000, y, color, ms = 5, mfc = 'k')
    plt.plot(int(row_vals[1]) / 100000, y, color )

plt.axis('off')
plt.show()