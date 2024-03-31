# 311-bike-lane-obstruction-extraction-system: unsupervised text classification
## What is the goal of this project?
Ask anyone who regularly moves about the city on their bike: infrastructure and lanes are often frustratingly blocked by parked vehicles or other obstructions, often in the same spots consistently. In many cities, the most that can be done in the moment is to take a photo and submit a 311 Illegal Parking Report. Even more frustratingly, these reports are not dealt with in a timely manner due to many reasons, with responses of the obstruction being clear sometimes being sent over a week after a report.
**What if there was a way to harness all of this data to better inform engineers of where infrastructure needs to be reinforced?**
By utilizing the [Lbl2Vec](https://wwwmatthes.in.tum.de/file/j6euhpir6wbc/Sebis-Public-Website/-/Semantic-Label-Representations-with-Lbl2Vec-A-Similarity-Based-Approach-for-Unsupervised-Text-Classification/Semantic%20Label%20Representations%20with%20Lbl2Vec.pdf) model, a varient of Word2Vec, unlabeled text can be classified into multiple classes based on keywords selected to represent the class. The cosine-similarity function is used on the document and label embeddings to determine the best label for the document. 
The current class and keyword breakdown is as shown below:
| Class:                     | Keyword(s):                   |
|----------------------------|-------------------------------|
| Bike lane obstruction      | bike, cycle, path             |
| Bus lane obstruction       | bus, stop                     |
| Non-resident parking       | resident, state               |
| Blocked Fire Hydrant       | fire, hydrant                 |
| Blocked Sidewalk           | sidewalk, side, walk          |
| Blocked Driveway           | driveway, drive, way, private |
| Blocked Crosswalk          | crosswalk, cross, walk        |
| Blocked Handicap Spot      | handicap, placard             |
| Double-Parking             | double, triple                |
| No stopping zone violation | stopping, zone                |
| Visitor Spot               | visitor, hour                 |
## What is the current status of the project?
The current phase being worked on is model evaluation and hyperparameter tuning. Because of the unlabeled nature of the data, evaluation is being done of models through evaluation of labels for ground-truth subsets for each class. The amount of classes and keywords for each class are also being examined during this process, as they can influence the performance of the Lbl2Vec model.
