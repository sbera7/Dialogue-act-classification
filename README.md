# About
This repository is on classifying the dialogue act of the sentences in a conversation. We are using SWDA and MRDA datasets for training the model.

# Dialogue-act-classification
In natural language understanding, a dialogue act characterizes the specific purpose served by an utterance within a conversational dialogue. These acts, falling under the umbrella of speech acts, manifest in diverse forms like questions, statements, or requests. The accurate prediction of dialogue acts plays a crucial role in the evolution of conversational agents, serving as a linchpin for enhancing dialog systems. In this repository, we conducted training using various deep learning algorithms, including CNN and LSTM, and employed different word embeddings to further advance our understanding and capabilities in this domain.

<table>
    <tr>
        <th>Speaker</th>
        <th>Utterance</th>
        <th>DA label</th>
    </tr>
    <tr>
        <td>A</td>
        <td>Okay.</td>
        <td>Other</td>
    </tr>
    <tr>
        <td>A</td>
        <td>Um. what did you do this weekend</td>
        <td>Question</td>
    </tr>
    <tr>
        <td>B</td>
        <td>Well, uh, pretty much spent most of my time in this yard</td>
        <td>Statement</td>
    </tr>
    <tr>
        <td>B</td>
        <td>[Throat Clearing]</td>
        <td>Non verbal</td>
    </tr>
    <tr>
        <td>A</td>
        <td>Uh Huh</td>
        <td>Backchannel</td>
    </tr>
    <tr>
        <td>A</td>
        <td>What do you have planned for your yard?</td>
        <td>Question</td>
    </tr>
    <tr>
        <td>B</td>
        <td>Well we are in the process of, realizing it</td>
        <td>Statement</td>
    </tr>
</table>



<h1 align="justify">Datasets</h1> 
<table>
  <tr>
    <th>Dataset</th>
    <th>Classes</th>
    <th>Vocabulary size</th>
    <th>Train size</th>
    <th>Val size</th>
    <th>Test size</th>
  </tr>
  <tr>
    <td>MRDA</td>
    <td>5</td>
    <td>10k</td>
    <td>75k</td>
    <td>16k</td>
    <td>16k</td>
  </tr>
   <tr>
    <td>SwDA</td>
    <td>43</td>
    <td>19k</td>
    <td>193k</td>
    <td>4k</td>
    <td>20k</td>
  </tr>
</table>
