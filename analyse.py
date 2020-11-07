import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import sys


def lighten_color(color, amount=0.1):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except KeyError:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])


if len(sys.argv) < 3:
    print("2 arguments required: datafile.csv title [export]")
    print(f"Given: {sys.argv}")
    exit(1)

if len(sys.argv) == 4:
    export_target = sys.argv[3]
else:
    export_target = None

title = sys.argv[2]

data = pd.read_csv(sys.argv[1], header=[0, 1], index_col=0)

patients = [f"UNI {i}" for i in [1, 2, 3, 7, 8, 9, 11, 12, 13]]
patients_names = [f"Patient {i+1}" for i, u in enumerate(patients)]
types = ["Patient", "Students"]
kinds = ["RIGHT", "BILATERAL", "LEFT",
         "Original parameters"
         ]
kindsc = ["red", "green", "darkorange", "blue"]
kindsc_s = [lighten_color(c) for c in kindsc]
print(patients)
print(types)

pat_data = []
stud_data = []
for p in patients:
    for k in kinds:
        pat_data.append(data[p][types[0]][k])
        stud_data.append(data[p][types[1]][k])

width = 0.4  # the width of the bars
print(pat_data)
print(stud_data)

ind = []
ind_pat = []
ind_lines = []
s = 0
for p in patients:
    pstart = s-1
    for k in kinds:
        ind.append(s)
        s = s+1
    ind_lines.append(s)
    ind_pat.append((pstart + s)/2)
    s = s+1
ind_lines.pop()


print(ind)
ind = np.array(ind)

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, pat_data, width,
                color=kindsc, edgecolor=kindsc, label='Patients')
rects2 = ax.bar(ind + width/2, stud_data, width,
                color=kindsc_s, edgecolor=kindsc, label='Students')

for x in ind_lines:
    ax.axvline(x=x, linestyle=":", color="grey")

ax.set_title(title, fontsize=24)
ax.set_xticks(ind_pat)
ax.set_xticklabels(patients_names)
ax.set_xlim(0-(width*2), ind[-1]+(width*2))
ax.set_ylim(-1000, 1000)


legend_elements = [
    Patch(facecolor='black', edgecolor='black', label='Patients'),
    Patch(facecolor=lighten_color("black"),
          edgecolor='black', label='Students'),
    Patch(facecolor='white', edgecolor='white', label='──────────────────')
]

for k, kc in zip(kinds, kindsc):
    legend_elements.append(Patch(facecolor=kc, label=k))
ax.legend(handles=legend_elements)

if export_target:
    fig.set_size_inches(12, 8.5)
    plt.tight_layout()
    plt.savefig(f'{export_target}.png', dpi=500)
    plt.savefig(f'{export_target}.pdf')
else:
    plt.show()
