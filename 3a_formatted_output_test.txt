import requests
import json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        

        if response.status_code == 200:
            result= response.json()
            emotions_dict= result["emotionPredictions"][0]["emotion"]
            dominant_emotion = max(emotions_dict, key=emotions_dict.get)
            emotions_dict["dominant_emotion"] = dominant_emotion 
            return emotions_dict
            
        elif response.status_code == 400:
            return {"error": "Blank text or invalid input provided."}
        else:
            return {
                "error": f"Request failed with status code {response.status_code}",
                "details": response.text
            }
            
    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred: {e}"}



