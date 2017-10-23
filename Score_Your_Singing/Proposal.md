# Music information retrieval (MIR)
## Definition and scope
## A brief history of MIR
â€¢ Don Byrd @ UMass Amherst + Tim Crawford @
Kingâ€™s College London receive funding for OMRAS
(Online Music Recognition and Searching)
â€“ Sp. 1999: Requested by NSF program director to organize
MIR workshop
â€¢ J. Stephen Downie + David Huron + Craig Nevill
Manning host MIR workshop @ ACM DL / SIGIR 99
â€¢ Crawford + Carola Boehm organize MIR workshop at
Digital Resources for the Humanities â€“ Sept. â€™99

â€¢ 2000: UMass hosts first ISMIR (International
Symposium on Music Information Retrieval)
â€“ Michael Fingerhut (IRCAM) creates music-ir mailing list
â€¢ ISMIR run as yearly conference
â€“ 2001: â€œSymposiumâ€ -> â€œConferenceâ€
â€¢ ISMIR incorporated as a Society in 2008
â€¢ MIREX benchmarking contest begun 2005
## Basic system overview
### Segmentatation
### Feature Extraction
### Analysis
# Feature representation
## Mel-Frequency Cepstral Coefficient (MFCC) 
measure of the timbre of a piece of music
representation of the short-term power spectrum of a sound, based on a linear cosine transform of a log power spectrum on a nonlinear mel scale of frequency.
MFCCs are commonly derived as follows:[1][2]

Take the Fourier transform of (a windowed excerpt of) a signal.
Map the powers of the spectrum obtained above onto the mel scale, using triangular overlapping windows.
Take the logs of the powers at each of the mel frequencies.
Take the discrete cosine transform of the list of mel log powers, as if it were a signal.
The MFCCs are the amplitudes of the resulting spectrum.
MFCCs are also increasingly finding uses in music information retrieval applications such as genre classification, audio similarity measures, etc.
MFCC values are not very robust in the presence of additive noise
## key
In music information retrieval, techniques have been developed to determine the key of a piece of classical Western music (recorded in audio data format) automatically. These methods are often based on a compressed representation of the pitch content in a 12-dimensional pitch-class profile (chromagram) and a subsequent procedure that finds the best match between this representation and one of the prototype vectors of the 24 minor and major keys (Purwins, Blankertz, and Obermayer 2000, 270â€“72). For implementation, often the constant-Q transform is used, displaying the musical signal on a log frequency scale. Although a radical (over)simplification of the concept of tonality, such methods can predict the key of classical Western music well for most pieces. Other methods also take into consideration the sequentiality of music.
## chords
## harmonies
## melody
## main pitch
## beats per minute or rhythm in the piece
## Tools
The Echo Nest We
send a song to their system, they analyze the acoustics and
provide 18 features to characterize global properties of the
songs
# Datasets
# Automatic Evaluation of Karaoke Singing
Karaoke is a popular form of singing entertainment, rooted from Japan. Many of nowaday karaoke systems have a scoring feature to evaluate singers’ performance. However, these rating is poorly constructed and not matched with human rating. Our project aims to provide an automatic evaluation based on appropriate acoustic features, extracted from the vocal signal of singers. Though speech processing is a very developed field of studies and techonologies, its approach is not suitable for singing voice because singing voice differs from speech in its intensity and dynamic range and because singing voice usually comes with a non stationary background music signal.
As we know, MIR can perform the tasks of labeling songs based on genre, mood, artists, etc. In this project, we focus on the vocal quality of the singing and train the machine to distinguish between good and poor singing. This can be done by recalling features of the singing, such as enthusiasm, emotion, pitch, volume, rythm, melodic similarity measures, etc.
## Music perception
Human can easily distinguish between music and noise. Phisically, music is ordered and patterned sound waves, produced by harmonic vibrations from the source. The major attibutes of music are as follows:
- The pitch value is determined by the wavelength of the sound signal. High-pitched tones have short wavelengths, while low-pitched tones have long wavelengths.
- Intensity, or loudness is to the magnitude of acoustic waves. High-magnitude sound carries more energy than low-magnitude sound.
- Duration refers to the amount of time in which a musical note sustain.
- Timbre refers to different harmonics, created by different source, e.g. piano vs. violin. 
## Feature extraction
To evaluate a piece of singing, we would like to combine both the score-based and machine-learned ranking methods. We first identify the perception which makes a piece of singing good or bad; it can be the enthusiasm of singers, which is mostly represented by intensity of the singings, or it can be the pitch interval, the vibrato, etc., or both. Then, we then link this perception to appropriate acoustic features. Alternatively, we can do a feature importance analysis among these acoustic features.

There are many features that can be extracted from music signal. These features can be categorized into: reference features, content-based features and text-based features. Reference features can be those relating to social interactions, e.g. followers, performance rating in, for example, soundcloud. Text-based features includes lyrics, interview, etc. Our approach will be based on content-based features, extracted from the wave signal, e.g. pitch, rythm, etc. and we might use reference features as ground truth for our machine-learned ranking method. 

The content-based features are calculated from low-level signal features (sometime refered as extraction methods), the most important of which is MFCC. MFCC and its derived features (such as ‘anchor space’[]) have been shown to give good performance for a variety of audio classification tasks. MFCCs capture the short-time spectral shape, which carries information about instrumental timbres or the quality of a singing. Yet, they do not capture long-term information such as melody, rhythm, etc. A study comparing audio feature extraction methods is conducted in [].
In this project, we do the feature extraction based on available toolboxes instead of doing low-level signal processing and transform (FFT, Wavelet, etc.). Some of toolboxes which could be used are described as follows:

Aubio: A library that extracts high level features such as beat tracking, tempo, melody.
Timbre Toolbox: A Matlab toolbox for high and low level feature extraction, providing different set of features to the MIR Toolbox, specifically made efficient for identifying timbre.
YAAFE: A library for Low level feature extraction, designed for computational efficiency and batch processing, written in C++ with a CLI and bindings for Python and Matlab.
pyAudioAnalysis: An open Python library that provides a wide range of audio-related functionalities focusing on feature extraction, classification, segmentation and visualization issues.
The Echo Nest Analyze API: An online system which can receive a song sent by users, analyze the acoustics and provide features to characterize global properties of the songs.

There are other tools, many of which are available to be evaluated in [].
## Related work
Music similarity metrics is a research aiming to calculate the similarity between songs or artists, comparing their performance. In [], authors employ a feature, derived from MFCC, called 'anchor space', which uses musical categories and well-known anchor artists as convenient reference points for describing features of the music. It is inspired by a fold wisdom such as "Jeff Buckley sounds like Van Morrison meets Led Zeppelin, but more folky." Other approaches for song similarity are to embed songs into a Euclidian metric space and do some distance-based analysis and clustering [].

For evaluation of karaoke singing, there is an approach based on the perception of singing enthusiasm []. The authors argue that karaoke is the form of entertainment for amateur so enthusiasm is a good criteria to evaluate them. They identified three acoustic features relevant to such perception: A weighted power, “fall-down”, and vibrato extent, developed a system for evaluating singing enthusiasm, and obtained a correlation coefficient of 0.65 between the system output and human evaluation. In our point of view, their method can be considered as score-based ranking. In [], the authors proposed a score combination from pitch-based, volume-based, and rhythm-based rating, with a reference specified karaoke song to evaluate a piece of singing. This approach is also score-based ranking. In [], the authors used HMM as a statistical music recognition model for automatic scoring of karaoke computer games. The musical features they employed are Pitch & Pitch Error, Accent, Zero-Crossing Rate, Root-Mean-Squared Energy.

Another effort for analyzing the singing voice is made in [], in which the authors reported good results of a system for classifying “good” and “poor” singing based on SVM. In [], the authors proposed a categorization and segmentation system for singing voice expression using pre-defined rules and HMM. There is another approach for automatic scoring of singing voice based on melodic similarity measures []. In [], a method of evaluating singing skills that does not require score information is represented. The authors used pitch interval accuracy and vibrato as acoustic features to evaluate singing. The approach was then tested by a 2-class (good/poor) classification test with 600 song sequences, and achieved an average classification rate of 83.5%. There is an approach for song classification based on perception of emtion [].
## Method and Model
Separation
of vocal and non-vocal segments of song, feature extraction
from singing part
### Learning to rank


Because feature vectors are computed from short segments of audio, an entire song induces a cloud of points
in feature space. The cloud can be thought of as samples from a distribution that characterizes the song,
and we can model that distribution using statistical techniques. Extending this idea, we can conceive of a
distribution in feature space that characterizes the entire repertoire of each artist.
We use Gaussian Mixture Models (GMMs) to model these distributions, similar to previous work [10].
Two methods of training the models were used: (1) the standard Expectation Maximization (EM) algorithm
for the GMM and (2) K-means clustering. Although unconventional, the use of K-means to train GMMs
was discovered to be useful to measure song-level similarity in previous work