# PitchTypeClassification
Simple Pitch Type Classification Project

This project takes unclassified trackman data for a single pitcher and uses clustering algorithms to assign pitch types to that data. 

Trackman data is part of MLB's Statcast system, and uses radar technology to get precise measurements on each pitch. These measurements include velocity at release, how much the pitch moves due to spin, the actual spin rate on the ball, and the direction of the ball's spin (sometimes called tilt). The information in Trackman can be used to distinguish different pitch types (i.e. fastball, curveball, slider, changeup, etc.), however prior some knowledge of the attributes of these different pitches is useful.

All steps from data import an cleaning to data exploration to the actual classification and validation of those classifications are demonstrated. The scope of the project was fairly small and straightforward, but this provides a demonstration of how to use trackman data to classify pitches.
