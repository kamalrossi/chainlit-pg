###########Chainlit##########
# This is the basic of chainlit app
#while you are given a loop,
#loop contains what you type and what 
#you will receive as feedback from 
#AI agent
##############################
import chainlit as cl


@cl.on_message
def main(message:str):
  you_typed=message.title()

  cl.send_message(aiagent_replied="Hey you typed:{you_typed}")    