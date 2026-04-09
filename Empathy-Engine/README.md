# Empathy Engine

The Empathy Engine is an AI-powered service that dynamically modulates synthesized speech based on the detected emotion of input text.

It bridges the gap between text sentiment and expressive speech output.

---

## Features

- Emotion Detection using Transformers
- Emotion-aware voice modulation
- Text-to-Speech generation
- Flask API
- Web interface with audio playback

---

## Technologies Used

Python  
Flask  
Transformers  
Google Text-to-Speech

Emotion detection model used:
HuggingFace emotion classification model

j-hartmann/emotion-english-distilroberta-base

---

## Project Architecture

User Input → Emotion Detection → Voice Modulation → Speech Generation → Audio Output

---

## Installation

Clone the repository

```bash
git clone https://github.com/Rakhi0402/Empathy-engine.git
cd Empathy-engine

