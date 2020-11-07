#!/usr/bin/env sh
rm -rf *.png *.pdf
python analyse.py anxiety.csv "Anxiety" "anxiety"
python analyse.py depressed_mood.csv "Depressed Mood" "depressed"
python analyse.py obsessions.csv "Obsessions" "obsessions"
python analyse.py compulsions.csv "Compulsions" "compulsions"
python analyse.py wellbeing.csv "General Wellbeing" "wellbeing"
python analyse.py avoidance.csv "Avoidance" "avoidance"

python analyse_single.py unvoluntary_motor_movements.csv "Unvoluntairy motor movements" unvoluntary_motor_movements
python analyse_single.py attention_memory_deficits.csv "Attention and memory deficits" attention_memory_deficits
python analyse_single.py restlessness_agitation.csv "Restlessness and Agitation" restlessness_agitation

python analyse_single_alt.py unvoluntary_motor_movements.csv "Unvoluntairy motor movements" unvoluntary_motor_movements_patient
python analyse_single_alt.py attention_memory_deficits.csv "Attention and memory deficits" attention_memory_deficits_patient
python analyse_single_alt.py restlessness_agitation.csv "Restlessness and Agitation" restlessness_agitation_patient

pdftk $(ls -tr *.pdf ) cat output out.pdf
