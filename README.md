# PitchTypeClassification
Simple Pitch Type Classification Project

This project takes unclassified trackman data for a single pitcher and uses clustering algorithms to assign pitch types to that data.

The included Trackman data (trackman_data.csv) comes from MLB's Statcast system which uses radar technology to get precise measurements on each pitch. These measurements include velocity at release, how much the pitch moves due to spin, the actual spin rate on the ball, and the direction of the ball's spin (sometimes called tilt). The information from Trackman can be used to distinguish different pitch types (i.e. fastball, curveball, slider, changeup, etc.), however some prior knowledge of the attributes of these different pitches is useful.

The code for all steps from data import and cleaning, to exploration, to the actual classification algorithm is found in the R Markdown file classification.Rmd. Classified_pitches.csv contains the classification for each pitch found trackman_data.csv. The final markdown document can be seen in classification.pdf. The scope of the project was fairly small and straightforward, but this provides a demonstration of how to use trackman data to classify pitches.
