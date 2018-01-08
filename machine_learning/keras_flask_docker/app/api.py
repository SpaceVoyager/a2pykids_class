#!flask/bin/python
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.datastructures import FileStorage

import numpy as np
from PIL import Image
from scipy.misc.pilutil import fromimage
from scipy.misc import imresize
import pickle

from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier


app = Flask(__name__)
api = Api(app)

kids = {
    'sophia': 'deer',
    'jerry': 'panda',
    'daniel': 'snail',
    'sean': 'rabbit'
}


def read_jpg(file_path):
    image = Image.open(file_path)
    if hasattr(image, '_getexif'):
        orientation = 0x0112
        exif = image._getexif()
        if exif is not None:
            orientation = exif[orientation]
            rotations = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }
            if orientation in rotations:
                image = image.transpose(rotations[orientation])

    img = fromimage(image, flatten=False, mode=None)
    # convert to gray-scale image
    img = img.mean(axis=2)
    return np.asarray(img, dtype=np.float32)


def load_one_face(face, resize=250, slice_=(slice(70, 195), slice(78, 172))):
    if resize is not None:
        face = imresize(face, (resize, resize))
        face = np.asarray(face[slice_], dtype=np.float32)
    return face


class CodeName(Resource):
    def get(self, name=None):
        if name is None or name == 'all':
            return kids
        else:
            if name not in kids:
                abort(404, message='I have never heard of ' + name)
            return {name: kids[name]}

    def post(self):
        json_data = request.get_json(force=True)
        if json_data['action'] == 'add_or_update':
            name = json_data['name']
            code_name = json_data['code_name']
            kids[name] = code_name
        elif json_data['action'] == 'delete':
            name = json_data['name']
            print name
            if name in kids:
                del kids[name]
        else:
            return "action not supported", 404
        return kids, 201


class FaceClassifier(Resource):
    def predict_face(self, img):
        some_face = load_one_face(img, resize=250, slice_=(slice(0, 250), slice(0, 250)))
        pkl_file = open('face_model.pkl', 'rb')
        face_model = pickle.load(pkl_file)
        pkl_file.close()
        target_names = ['Daniel Zhang', 'Sophia Wang', 'sean xie']

        predicted_label = face_model.predict([some_face.flatten()])[0]

        return target_names[predicted_label]

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('photo', type=FileStorage, location='files')
        args = parse.parse_args()
        stream = args['photo'].stream
        img = read_jpg(stream)

        return {'predicted face': self.predict_face(img)}


api.add_resource(CodeName, '/', '/<name>')
api.add_resource(FaceClassifier, '/whoisit')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

