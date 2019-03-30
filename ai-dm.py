import fire
import json
import os
import numpy as np
import tensorflow as tf

import model, sample, encoder


def text_replace(text):
# Replace certain words
    text = text.replace("I ","you ")
    text = text.replace("we ","you ")
    text = text.replace("We ","You ")
    text = text.replace(" mine"," yours")
    text = text.replace("kill you", "hurt you")
    text = text.replace("[","")
    text = text.replace("]","")
    return text



def interact_model(
    model_name='117M',
    seed=None,
    nsamples=4,
    batch_size=1,
    length=80,
    temperature=0.8,
    top_k=0,
):
    """
    Interactively run the model
    :model_name=117M : String, which model to use
    :seed=None : Integer seed for random number generators, fix seed to reproduce
     results
    :nsamples=1 : Number of samples to return total
    :batch_size=1 : Number of batches (only affects speed/memory).  Must divide nsamples.
    :length=None : Number of tokens in generated text, if None (default), is
     determined by model hyperparameters
    :temperature=1 : Float value controlling randomness in boltzmann
     distribution. Lower temperature results in less random completions. As the
     temperature approaches zero, the model will become deterministic and
     repetitive. Higher temperature results in more random completions.
    :top_k=0 : Integer value controlling diversity. 1 means only 1 word is
     considered for each step (token), resulting in deterministic completions,
     while 40 means 40 words are considered at each step. 0 (default) is a
     special setting meaning no restrictions. 40 generally is a good value.
    """
    if batch_size is None:
        batch_size = 1
    assert nsamples % batch_size == 0

    enc = encoder.get_encoder(model_name)
    hparams = model.default_hparams()
    with open(os.path.join('models', model_name, 'hparams.json')) as f:
        hparams.override_from_dict(json.load(f))

    if length is None:
        length = hparams.n_ctx // 2
    elif length > hparams.n_ctx:
        raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

    with tf.Session(graph=tf.Graph()) as sess:
        context = tf.placeholder(tf.int32, [batch_size, None])
        np.random.seed(seed)
        tf.set_random_seed(seed)
        output = sample.sample_sequence(
            hparams=hparams, length=length,
            context=context,
            batch_size=batch_size,
            temperature=temperature, top_k=top_k
        )

        saver = tf.train.Saver()
        ckpt = tf.train.latest_checkpoint(os.path.join('models', model_name))
        saver.restore(sess, ckpt)
        print("")
        print("=" * 40 + "  "+ "=" * 40)  

        last_paragraph = "You enter a dungeon with your trusty sword and shield. You are searching for your true desire which you know is at the lowest level of this dungeon. You know you will encounter goblins and ogres. You enter the first door and see "
        print(last_paragraph)
        raw_text = last_paragraph
    
        context_tokens = enc.encode(raw_text)
        out = sess.run(output, feed_dict={
                context: [context_tokens for _ in range(1)]
            })[:, len(context_tokens):]

        text = enc.decode(out[0])
        last_period = text.rfind('.')
        text = text[0:last_period+1]
        text = text_replace(text)
        
        raw_text = text
        print(raw_text)
        print(" ")
        
        prefixes = ["You attack ", "You tell them", "You use", "You go"]

        while True:
            
            last_paragraph = raw_text
            generated = 0  
            options = []        
            
            print("=" * 40 + "  "+ "=" * 40)  
            
            for j in range(nsamples // batch_size):
            
                raw_text = raw_text + prefixes[j]
                context_tokens = enc.encode(raw_text)
                out = sess.run(output, feed_dict={
                    context: [context_tokens for _ in range(batch_size)]
                })[:, len(context_tokens):]
              
                generated += 1
                text = enc.decode(out[0])
                text = prefixes[j] + text
                first_period = text.find('.')
                text = text[0:first_period+1]
                text = text_replace(text)
                
                options.append(text)
                
               
            for i, option in enumerate(options):

                print(str(i)+") ", option)
        
                
            choice = input("Which do you choose? (0/1/2/3) ")
            print(" ")
            print(options[int(choice)])
            print(" ")

            # Compute result
            raw_text = last_paragraph + options[int(choice)]
            context_tokens = enc.encode(raw_text)
            out = sess.run(output, feed_dict={
                    context: [context_tokens for _ in range(1)]
                })[:, len(context_tokens):]

            text = enc.decode(out[0])
            last_period = text.rfind('.')
            text = text[0:last_period+1]
            text = text_replace(text)
            
            raw_text = text
            print(raw_text)
            


if __name__ == '__main__':
    fire.Fire(interact_model)
