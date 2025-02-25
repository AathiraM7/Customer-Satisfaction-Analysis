#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd 

data = pd.read_csv(r"C:\Users\user\Desktop\Projects\e commerce dataset.csv" )


print(data.head())


# In[36]:


print(data.describe())                                                            


# # Data Visualization 

# In[54]:


import matplotlib.pyplot as plt 

numeric_cols = ['Age','PurchaseAmount', 'PurchaseFrequency','ProductQualityRating','DeliveryTimeRating','CustomerServiceRating','WebsiteEaseOfUseRating','ReturnRate','DiscountUsage']

plt.figure(figsize=(15,20))

for i,col in enumerate(numeric_cols,1):
    plt.subplot(5,2,i)
    plt.hist(data[col],bins=20,color='green',edgecolor='r',alpha=0.7)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# In[55]:


#create age groups 

bins = [18,30,40,50,60,70]
labels = ['18-29','30-39','40-49','50-59','60-69']
data['AgeGroup'] = pd.cut(data['Age'],bins=bins,labels=labels,right=False)

numeric_columns =['ProductQualityRating','DeliveryTimeRating','CustomerServiceRating','WebsiteEaseOfUseRating']

mean_ratings_age_gender = data.groupby(['AgeGroup','Gender'])[numeric_columns].mean()

mean_ratings_age_gender.reset_index(inplace=True)
print(mean_ratings_age_gender)


# In[56]:


numeric_columns =['ProductQualityRating','DeliveryTimeRating','CustomerServiceRating','WebsiteEaseOfUseRating','ReturnRate','DiscountUsage']

mean_ratings_loyalty = data.groupby('LoyaltyProgramMember')[numeric_columns].mean()

mean_ratings_loyalty.reset_index(inplace=True)
print(mean_ratings_loyalty)


# In[57]:


data['NPS_Category'] = pd.cut(data['CustomerServiceRating'],bins=[0,6,8,10],labels=['Detractors','Passives','Promoters'],right=False)

nps_counts = data['NPS_Category'].value_counts(normalize=True)*100
nps_score = nps_counts['Promoters'] - nps_counts['Detractors']

nps_counts


# In[58]:


nps_score


# In[66]:


low_rating_threshold = 2 

low_product_quality = data[data['ProductQualityRating'] <= low_rating_threshold]
low_delivery_time = data[data['DeliveryTimeRating'] <= low_rating_threshold]
low_customer_service = data[data['CustomerServiceRating'] <= low_rating_threshold]
low_website_ease_of_use = data[data['WebsiteEaseOfUseRating'] <= low_rating_threshold]

plt.figure(figsize=(20,15))

plt.subplot(2,2,1)
plt.hist([low_product_quality['Age'],low_delivery_time['Age'],low_customer_service['Age'],low_website_ease_of_use['Age']],bins=10,label = ['Product Quality','Delivery Time','Customer Service','Website Ease of Use'])

plt.title('Age Distribution for Low Ratings')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()


plt.subplot(2,2,2)
plt.hist([low_product_quality['PurchaseAmount'],low_delivery_time['PurchaseAmount'],low_customer_service['PurchaseAmount'],low_website_ease_of_use['PurchaseAmount']],bins=10,label = ['Product Quality','Delivery Time','Customer Service','Website Ease of Use'])
plt.title('Purchase Amount Distribution for Low Ratings')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(2,2,3)
plt.hist([low_product_quality['PurchaseFrequency'],low_delivery_time['PurchaseFrequency'],low_customer_service['PurchaseFrequency'],low_website_ease_of_use['PurchaseFrequency']],bins=10,label = ['Product Quality','Delivery Time','Customer Service','Website Ease of Use'])
plt.title('Purchase Frequency Distribution for Low Ratings')
plt.xlabel('Purchase Frequency')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(2,2,4)
plt.hist([low_product_quality['ReturnRate'],low_delivery_time['ReturnRate'],low_customer_service['ReturnRate'],low_website_ease_of_use['ReturnRate']],bins=10,label = ['Product Quality','Delivery Time','Customer Service','Website Ease of Use'])
plt.title('Return Rate Distribution for Low Ratings')
plt.xlabel('Return Rate')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()


# In[ ]:




