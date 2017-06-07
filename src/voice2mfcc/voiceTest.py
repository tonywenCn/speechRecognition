import librosa
import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt

y, sr = librosa.load(librosa.util.example_audio_file())
z = y[1355168-100000:1355168-100000+10000]
x = np.ones((2, z.shape[0]))

for i in xrange(x.shape[1]):
    x[0][i] = i

plt.plot(x[0], z)
plt.savefig("voiceWave.png")
