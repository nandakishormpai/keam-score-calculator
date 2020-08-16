from flask import Flask, render_template, request, redirect,flash
app = Flask(__name__)

import myapp.views
