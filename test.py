import pymongo
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
from flask import Flask
from flask import request
myclient = pymongo.MongoClient("mongodb+srv://root:eZcu9qthj7GgmNMY@smartourist.foiibut.mongodb.net")