<h1>About</h1>
<p align="justify">This jupyter notebook is about classifying the dialogue act in a sentence. The model is trained on the SwDA and MRDA dataset.</p>



<h1 align="justify">Dialogue-act-classification</h1>
<p align="justify">In Natural language understanding, a dialog act is an utterance, in the context of a conversational dialog, that serves the function in the dialog. Dialog act are a type of speech act. Types of dilog acts may include question, statement or a request. The task of predicting dialog acts(DA) based on dialog system is a key factor in the development of conversational agents.
<br></br>


</p>
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
