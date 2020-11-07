import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import sys


if len(sys.argv) < 3:
    print("2 arguments required: datafile.csv title [export]")
    print(f"Given: {sys.argv}")
    exit(1)

if len(sys.argv) == 4:
    export_target = sys.argv[3]
else:
    export_target = None

title = sys.argv[2]

data = pd.read_csv(sys.argv[1], header=[0], index_col=0)

patients = [f"UNI {i}" for i in [1, 2, 3, 7, 8, 9, 11, 12, 13]]
patients_names = [f"Patient {i+1}" for i, u in enumerate(patients)]
kinds = ["RIGHT", "BILATERAL", "LEFT",
         "Original parameters"
         ]
kindsc = ["red", "green", "darkorange", "blue"]
print(patients)

pat_data = []
pat_c = []


ind = []
ind_pat = []
ind_lines = []
s = 0

for i, k in enumerate(kinds):
    pstart = s-1
    for p in patients:
        ind.append(s)
        s = s+1
        pat_data.append(data[p][k])
        pat_c.append(kindsc[i])
    ind_lines.append(s)
    ind_pat.append((pstart + s)/2)
    s = s+1
ind_lines.pop()

width = 0.4  # the width of the bars
print(pat_data)


print(ind)
ind = np.array(ind)

fig, ax = plt.subplots()
rects1 = ax.bar(ind, pat_data, width,
                color=pat_c, edgecolor=pat_c, label='Patients')

for x in ind_lines:
    ax.axvline(x=x, linestyle=":", color="grey")

ax.set_title(title, fontsize=24)
ax.set_xticks(ind_pat)
ax.set_xticklabels(kinds)
ax.set_xlim(0-(width*2), ind[-1]+(width*2))
ax.set_ylim(-1000, 1000)

for i, pos in enumerate(ind):
    v = pat_data[i]
    ax.text(pos, y=-950, s=(i % 9)+1, c="gray",
            horizontalalignment='center', verticalalignment='center',
            )

legend_elements = []

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
