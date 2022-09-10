from textwrap import indent
from deepgram import Deepgram
import asyncio, json

# The API key you created in step 1
DEEPGRAM_API_KEY = 'e10348a742ae9dc36c7fea998a1ff4088f254c8d' #'294dad26b6f53b7ba9e4dd4a6b3eb48f3cac44a0'

# Replace with your file path and audio mimetype
PATH_TO_FILE = '/Users/sankalpbhatia/Dropbox/Mac/Desktop/GME_earnings_call.wav'
MIMETYPE = 'audio/wav'

async def main():
    # Initializes the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    
    with open(PATH_TO_FILE, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': MIMETYPE}
        options = { "punctuate": True, "model": "finance", "tier":"enhanced", "language": "en", "diarize":True, "tier": "enhanced", "sentiment":True, "numerals":True }
    
        print('Requesting transcript...')
        print('Your file may take up to a couple minutes to process. \n')

        response = await dg_client.transcription.prerecorded(source, options)
        #print(type(response))
        #print(type(json.dumps(response, indent=4)))
        #print(type(response))
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']

        #global sentence_list
        sentence_list = transcript.split(". ")
        return sentence_list
        #print(sentence_list)
        #print(type(sentence_list))

#print(sentence_list)
response = asyncio.run(main())
print(response)