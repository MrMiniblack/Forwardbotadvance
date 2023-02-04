import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "22456077"))
    API_HASH = os.environ.get("API_HASH", "ac0947297bfd7e83be7e1f311c7c4171")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1420828558")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Adityabot:2005@cluster0.2ouvf2v.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQABVBUYKIGQ8xjAO9BfBQkk6GtFZhrYYIzgxBYJAIXtB7ZvodIDv2hDl3wNyCETic-qQvpgsmT_-tw2IQmx3YUC5njAI319FaKSsz_zcIpxj0-O-4JHeo1Ui52Nc6C_SqTWeXytP3Lm2QmBW_RPQ9z-Gv_y0aT6sigbHA9xIXTWoUv136e0QbPGtqxflBwAJT8yTv9Sb76eNRqEW3SnR9pwGrHt05FTto4sqjTSqFLVCmRBhSkTNGTC3CH1Ld0YJUM3e40H_JczDcyuWkwC5bPAVMcIivPWTDGfQQHH1iDCEeaqrdgpUB8jhDnMGbUZIq_Hc5vJN8s1XNIo26JNmkyNAAAAAFSwH44A")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001807817046"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Advance_forward_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
