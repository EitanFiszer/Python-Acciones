import tweepy

#Claves de acceso a la API de Twitter (Chiqui_Patria)
api_key = "oVkZn2ogpUSY0XDyeqNAAqsxw"
api_secret = "QT6H8wK2M1smkv3aSnmZ7g0lL9npgz8mdRvLmA0O886ilrECse"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPMZyAEAAAAAPqVQS5Ui%2FpCuiFEnqHcEagf9Heo%3DBfEcLgx2IxOc5maqJiWottREbGTOwo6Jru7msMJ8sncED9y9QS"
access_token = "1614746822970327042-3AXsNSS1fu6brFrFDLbt3pRamOYIs8"
access_token_secret = "uFAliD3cNlx91dvI5ZCa6GqwNNaDmFHLYfvaRWtMSHIY9"


#Autenticación con Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#Funcion para twittear lo que haga falta
def tweetear(contenido):
    client.create_tweet(text=contenido)