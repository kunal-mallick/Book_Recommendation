# Book_Recommendation

We are proud to introduce our new book recommendation system, book.io. This system uses the **user-to-user collaborative filtering model**  to recommend books to users based on their preferences and ratings. 

Our system recommends 10 books to each user: 5 based on the user's geographical area and 5 based on the user's age group. For each of these categories, we have built 6 different models to cater to different segments of users. For example, in the area-based category, we have models for the USA, Canada, UK, Australia, Germany, and other countries. Similarly, in the age-based category, we have models for adults, teenagers, younger, elder, children, and other age groups.

Our system aims to provide personalized and relevant book recommendations to our users, by leveraging the similarities between users and items simultaneously. We hope you enjoy using book.io and discover new books that match your interests and tastes.
> Live demo [_here_](https://book-recommendation.streamlit.app/)

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!--* [License](#license) -->


## General Information
We are proud to introduce book.io, a book recommendation system that uses the user-to-user collaborative filtering model. Here are some features of our system:

- It recommends 10 books to each user, based on their preferences and profile.
- It uses two criteria to select the books: the user's geographic area and age group.
- It has six different models for each criterion, covering various regions and demographics. For example, 
    - It has models for the USA, Canada, UK, Australia, Germany, and other countries for the area-based criterion.
    - It has models for adults, teenagers, younger, elder, children, and other age groups for the age-based criterion.
- It updates the recommendations regularly based on the user's feedback and

## Technologies Used
- Language Used : Jupyter Notebook(Python), CSS

- libraries used
    - Data Preprocessing & EDA :numpy, pandas, matplotlib, seaborn, re
    - Model Building :numpy, pandas, pickle, sklearn.metrics(pairwise_distances)
    - Deployment : pickle, pandas, streamlit
    - Server Deployment : https://share.streamlit.io/


## Screenshots
![Top]()
![mid]()
![bottom]()


## Setup
- For Online [click here](https://book-recommendation.streamlit.app/)

- For Offline download everything in requirements.txt and then open the anaconda / python terminal and run this line of code :
 
```bash
cd file path
```
```bash
streamlit run main.py
```


## Project Status
Project is: Deployed

## Room for Improvement

Room for improvement:
- Creating New Model
- Improving UI 
- Creating Search Feature


## Acknowledgements
- Many thanks to
    - [w3schools](https://www.w3schools.com/)
    - [geeksforgeeks](https://www.geeksforgeeks.org/)
    - [coolors](https://coolors.co/palettes/trending/rainbow)
    - [figma](https://www.figma.com/)


## Contact
Created by [@kunal](https://github.com/kunal-mallick) - feel free to contact me!


<!-- Optional 
## License
This project is open source and available under the [MIT License](https://github.com/kunal-mallick/Water-Quality/blob/main/LICENSE).

<!-- You don't have to include all sections - just the one's relevant to your project -->
