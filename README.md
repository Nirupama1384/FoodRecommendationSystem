# FoodRecommendationSystem
A Recommendation system which suggests food items to the users considering different factors like user preferences, time, item-similarity based etc.,
User is verified, if the user has previous orders, we will fetch data from the user’s previous orders. Tags corresponding to the user’s previous orders are extracted from orders and food csv file. We will scale down the tags based on those orders and find food items with similar tags from the food file. Scale them down to the most ordered or most popular items and recommend them to the user. If the user doesn’t have any previous order history, we recommend popular and special items to the user, when he wants to order.
When we extract these tags from user’s previous orders and current recommendations which we made for the user, if majority of the tags are similar to those of previous orders, we will increase the count of true positive, if not we increase the false negative count.
Accuracy is found from these true positive and false negative counts. Average accuracy is found to be around 85\% for 16 users.
