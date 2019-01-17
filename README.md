# Recon-all Processing Time
Looking at how long the freesurfer longitudinal pipeline takes.

All processing was completed on the [Bianca](http://www.uppmax.uu.se/resources/systems/the-bianca-cluster/) HPC, which is part of the [Swedish National Infrastructure for Computing](https://www.snic.se/).
<br>
I have yet to be able to figure out how to do multi-node parallizaton with freesurfer.
I found many helpful resources on parallization that work within node.

<br>

The data is not directly comparable, since there is attrition due to failed scans!

```cat reconall_bianca/sim_subs_r.txt | parallel "tail -n1 /proj/sens2018615/imagen_longpipe/{}/scripts/recon-all.log | grep 'without error'" | awk '{print $3}' | parallel "tail -n2 /proj/sens2018615/imagen_longpipe/{}/scripts/recon-all.log | head -n1" | awk '{print $3}' > base_time.txt```

