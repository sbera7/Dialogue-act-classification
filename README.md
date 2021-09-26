<h1>About</h1>
<p align="justify">This repo contains implementation of basic ideas of sequencial models(such as LSTM, attention) on detecting DA in pyhton using keras layers.</p>



<h1 align="justify">Dialogue-act-classification</h1>
<p align="justify">In Natural language understanding, a dialog act is an utterance, in the context of a conversational dialog, that serves the function in the dialog. Dialog act are a type of speech act. Types of dilog acts may include question, statement or a request. The task of predicting dialog acts(DA) based on dialog system is a key factor in the development of conversational agents.</p>

<h1 align="justify">Literary work</h1>
<p align="justify">Several approaches have been proposed to tackle the DA classification problem. These methods can be divided into two different categories. The first type of methods relies on the independent classification of each utterance using various techniques, such as HMM(Stolcke et al. 2000), SVM (Surendran and Levow 2006) and Bayesian Network (Keizer, op den Akker, and Nijholt 2002).And the second type, which achieves better performance, leverages the context, to improve the classifier performance by using deep learning approaches to capture contextual dependencies between input sentences (Bothe et al. 2018; Khanpour, Guntakandla, and Nielsen 2016). Another refinement of input contextbased classification is the modelling of inter-tag dependencies. This task is tackled as sequence based classification where output tags are considered as a DA sequence (<a href="https://arxiv.org/abs/1904.08637"> Li et al. 2018a</a>;<a href="https://arxiv.org/abs/1810.09154">Kumar et al. 2018</a>  <a href="https://aclanthology.org/J00-3003/">Stolcke et al. 2000</a>; <a href="https://arxiv.org/abs/1810.09154">Chen et al. 2018</a>;<a href="https://arxiv.org/abs/1904.02594">link Raheja and Tetreault 2019</a> ). The current state of art model(<a href="https://arxiv.org/abs/2002.08801">Colombo et al., 2020)</a>. It makes an approach to leverage seq2seq widely adopted in neural machine translation(NMT) to improve the modelling of tag sequentiality with a guided attention mechanism and beam search applied to both training and inference. This proposed approach achieves an accuracy score of 85% on SwDA, and state-of-the-art accuracy score of 91.6% on MRDA.</p>


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
