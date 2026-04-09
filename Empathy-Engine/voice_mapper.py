def map_emotion_to_voice(emotion, confidence):

    base_rate = 150

    if emotion == "joy":
        rate = base_rate + int(40 * confidence)
        volume = 1.0

    elif emotion == "sadness":
        rate = base_rate - int(40 * confidence)
        volume = 0.7

    elif emotion == "anger":
        rate = base_rate + int(20 * confidence)
        volume = 1.0

    elif emotion == "fear":
        rate = base_rate - int(20 * confidence)
        volume = 0.8

    elif emotion == "surprise":
        rate = base_rate + int(30 * confidence)
        volume = 0.9

    else:
        rate = base_rate
        volume = 0.85

    return rate, volume