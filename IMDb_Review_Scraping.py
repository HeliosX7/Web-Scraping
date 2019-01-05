from bs4 import BeautifulSoup
from urllib.request import urlopen
from re import findall

def get_review(url):
    html=urlopen(url).read()
    soup=BeautifulSoup(html,"html.parser")

    print("\n|| Critic Reviews ||\n")
    
    movie_name=soup.findAll("h3",{"itemprop":"name"})
    print("Movie : "+movie_name[0].text)
    
    find_metascore=soup.findAll("div",{"class":"metascore_wrap"})
    metascore=findall("\d+",str(find_metascore))
    print("Metascore : "+metascore[0]+"\n\n\n")
  
    #grab each review
    reviews_1=soup.findAll( "tr",{"class":"even detailed"} )

    reviews_2=soup.findAll( "tr",{"class":"odd detailed"} )

    
    for each in reviews_1:

       user=each.findAll("span",{"itemprop":"name"})
       print("User : "+user[0].text + " " + user[1].text+"\n")

       find_rating=each.findAll("span",{"itemprop":"ratingValue"})
       rating=findall("\d+",str(find_rating))
       print("Rating : "+rating[0]+"\n")
       
       review=each.findAll("div",{"class":"summary"})
       print("Review : " +review[0].text+"\n\n")



    for each in reviews_2:

       user=each.findAll("span",{"itemprop":"name"})
       print("User : "+user[0].text + " " + user[1].text+"\n")

       find_rating=each.findAll("span",{"itemprop":"ratingValue"})
       rating=findall("\d+",str(find_rating))
       print("Rating : "+rating[0]+"\n")
       
       review=each.findAll("div",{"class":"summary"})
       print("Review : " +review[0].text+"\n\n")


  
    
link=input("Enter the url:")

get_review(link)


