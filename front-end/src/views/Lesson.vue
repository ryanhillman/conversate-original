<template>
  <div v-if="user">
    <header>Select any lesson to begin!</header>
    <!--Lesson 1 avere and essere -->

    <div class="individual-lesson">
      <label for="avere-essere">Avere and Essere: </label>
      <button id="avere-essere" value="ShowLesson1" @click="toggleLesson1">
        Toggle Lesson
      </button>
      <div v-if="toggleL1 === true">
        <h1>Lesson 1: <i>Avere</i> and <i>Essere</i></h1>
        <h3>To have and to be</h3>
        <p>
          Two of the most important verbs in the italian language are
          <strong>avere</strong> (to have) and <strong>essere</strong> (to be).
          These two auxiliary verbs are both extremely common in every day use,
          as well as having many different uses to supplement other verbs and
          tenses throughout the italian language.
        </p>
        <h4>Avere</h4>
        <ul>
          <li>io - {{ avere.io }}: I have</li>
          <li>tu - {{ avere.tu }}: you have</li>
          <li>lui/lei - {{ avere.lui }}: he or she has</li>
          <li>noi - {{ avere.noi }}:we have</li>
          <li>voi - {{ avere.voi }}:You all have</li>
          <li>loro - {{ avere.loro }}:They have</li>
        </ul>
        <h5>Examples uses</h5>
        <ul>
          <li>"Ho un gatto. " --> I have a cat.</li>
          <li>"Hai un umbrello." --> you have an umbrella.</li>
          <li>"Lei ha due fratelli." --> She has two brothers.</li>
          <li>
            "Abbiamo pesce per cena stasera." --> We have fish for dinner
            tonight.
          </li>
          <li>
            "Voi avete ritornare domani." --> You all have to return tomorrow.
          </li>
          <li>"Loro hanno troppo cibo!" --> They have too much food!</li>
        </ul>
        <p>
          It's important to become familiar with the verb avere, because not
          only does it function to show possession or ownership, but it assists
          as an auxiliary verb to many other verbs and tenses in the italian
          language, so learning it early on is an important fundamental step to
          mastering the language.
        </p>
        <h4>Essere</h4>
        <ul>
          <li>io - {{ essere.io }}: I am</li>
          <li>tu - {{ essere.tu }}: you are</li>
          <li>lui/lei - {{ essere.lui }}: she or he is</li>
          <li>noi - {{ essere.noi }}: we are</li>
          <li>voi - {{ essere.voi }}: you all are</li>
          <li>loro - {{ essere.loro }}: they are</li>
        </ul>
        <h5>Example uses</h5>
        <ul>
          <li>"Sono un umane." --> I am a human.</li>
          <li>"Sei in ritardo" --> You are late.</li>
          <li>"E bene?" --> it's okay?</li>
          <li>"Siamo in le montagne." --> We are in the mountains.</li>
          <li>"siete ragazzi alti." --> You are tall kids.</li>
          <li>"Loro sono molto gentili"--> They are very kind.</li>
        </ul>
        <p>
          It's also imporant to familiarize yourself with the verb essere, as,
          like avere, it functions as an auxiliary verb to many of the different
          tenses and verbs in the italian language, so again, mastering this
          verb early on will be a fundamental step in mastering the Italian
          language.
        </p>

        <h5>Now let's practice some on your own!</h5>

        <label for="question1">We have:</label>
        <input v-model="answer1"
          :class="{ wrong: answer[0] !== avere.noi }"
          type="text"
          id="question1"
          name="question1"
          v-model.trim="answer[0]"
        />
        <p></p>
        <label for="question2">They are:</label>
        <input
          :class="{ wrong: answer[1] !== essere.loro }"
          type="text"
          id="question2"
          name="question2"
          v-model.trim="answer[1]"
        />
        <p></p>
        <label for="question3">I have:</label>
        <input
          :class="{ wrong: answer[2] !== avere.io }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[2]"
        />
        <p></p>
        <label for="question4">You are:</label>
        <input
          :class="{ wrong: answer[3] !== essere.tu }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[3]"
        />
        <p></p>
        <label for="question5">You all have:</label>
        <input
          :class="{ wrong: answer[4] !== avere.voi }"
          type="text"
          id="question5"
          name="question5"
          v-model.trim="answer[4]"
        />
        <p></p>
        <label for="question6">They have:</label>
        <input
          :class="{ wrong: answer[5] !== avere.loro }"
          type="text"
          id="question6"
          name="question6"
          v-model.trim="answer[5]"
        />
      </div>
    </div>
    <!-- lesson 2 Basic Greetings -->
    <div class="individual-lesson">
      <label for="basic-greetings">Basic Greetings: </label>
      <button id="basic-greetings" value="ShowLesson2" @click="toggleLesson2">
        Toggle Lesson
      </button>
      <div v-if="toggleL2">
        <h1>Lesson 2: <i>Basic Greetings</i></h1>
        <h3>Ciao!</h3>
        <p>
          On of the most important phrases, and one you perhaps already use in
          your own vocabulary, is the phrase "ciao". In italian, ciao can
          mastering both hello and goodbye and is typically used in mostl
          informal settings.
        </p>
        <p>Some different ways to use ciao</p>
        <ul>
          <li>"Ciao bella" --> Hello beautiful</li>
          <li>
            "Ciao ciao, come stai oggi?" --> Hello hello, how are you today?
          </li>
        </ul>
        <p>
          In order to avoid being repetive, it's important to learn more than
          just one way to say hello.
        </p>
        <h4>Common Greetings</h4>
        <ul>
          <li>
            Buongiorno! --> Goodmorning
            <p>Typically only used before noon</p>
          </li>
          <li>
            Buon pomoriggio! --> Good afternoon
            <p>Typically used from noon to around 3 in the afternoon</p>
          </li>
          <li>
            Buona sera!
            <p>Typically used after 4 or 5 in the afternoon.</p>
          </li>
          <li>
            Salve!
            <p>
              Similar to ciao, salve can be both hello and goodbye, but is the
              formal use.
            </p>
          </li>
        </ul>
        <h5>Greeting examples</h5>
        <ul>
          <li>
            "Buongiorno, come stai oggi?" --> Goodmorning! How are you today?
          </li>
          <li>"Buon pomoriggio ragazzi!" --> Good afternoon kids!</li>
          <li>
            "Buona sera signore Valentino!" --> Good evening Mr. Valentino.
          </li>
          <li>"Ciao ciao, Come va?" --> Hi hi, how's it going?.</li>
        </ul>
        <p>
          Because greeting someone is one of the first things you do when
          visiting another country, it's important that you have multiple ways
          in doing in order to avoid becoming redundant in your greetings.
        </p>

        <h5>Now let's practice some on your own!</h5>

        <label for="question1">Ciao:</label>
        <input
          :class="{ wrong: answer[0] !== 'hi' }"
          type="text"
          id="question1"
          name="question1"
          v-model.trim="answer[0]"
        />
        <p></p>
        <label for="question2">Buona Sera: </label>
        <input
          :class="{ wrong: answer[1] !== 'good evening' }"
          type="text"
          id="question2"
          name="question2"
          v-model.trim="answer[1]"
        />
        <p></p>
        <label for="question3">Buon pomoriggio</label>
        <input
          :class="{ wrong: answer[2] !== 'good afternoon' }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[2]"
        />
        <p></p>
        <label for="question4">Buongiorno!</label>
        <input
          :class="{ wrong: answer[3] !== 'good morning' }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[3]"
        />
      </div>
    </div>
    <!-- Lesson 3 begins here -->
    <div class="individual-lesson">
      <label for="essere-versus-stare">Essere versus Stare: </label>
      <button
        id="essere-versus-stare"
        value="ShowLesson3"
        @click="toggleLesson3"
      >
        Toggle Lesson
      </button>
      <div v-if="toggleL3">
        <h1>Lesson 3: <i>Essere vs. Stare</i></h1>
        <h3>Stare (to be)</h3>
        <p>
          Stare is a similar verb to essere in literal meaning, but their uses
          can vary widly depending on the situation that is being presented.
        </p>
        <h5>
          Let's begin by talking about the differences between the two verbs.
        </h5>
        <p>
          When to use Essere: When discussing permenance. A good rule of thumb
          to follow is that when the object being discussed is of a permanent or
          non transient type the default verb to use in this circumstance would
          be essere. Stare uses tend to be less permanent and subject to change,
          for examples how someone is feeling currently.
        </p>
        <ul>
          <li>
            When expressing your nationality:
            <p>
              "Ciao,Sono Paulo e sono Tedesco" --> Hi, I'm Paulo and I am
              German.
            </p>
          </li>
          <li>
            Identifying ones profession:
            <p>"Sono un avvocato!" --> I am a lawyer!</p>
          </li>
          <li>
            Describing ones physical appearance.
            <p>"Sono basso e grasso" --> I am short and fat.</p>
          </li>
          <li>
            Describing and locating objects
            <p>"Dov'e lo zucchero?" --> Where is the sugar?</p>
          </li>
        </ul>
        <p>
          First, let's learn to conjugate the verb <i>stare</i> so that we can
          see how it is used.
        </p>
        <ul>
          <li>io: {{ stare.io }} --> I am</li>
          <li>tu: {{ stare.tu }} --> You are</li>
          <li>lui/lei: {{ stare.lui }} --> He or she is</li>
          <li>noi: {{ stare.noi }} --> We are</li>
          <li>voi: {{ stare.voi }} --> You all are.</li>
          <li>loro: {{ stare.loro }} --> They are</li>
        </ul>
        <p>
          In contrast to <i>essere</i> the verb stare as a general rule of thumb
          has to do with transient states or temporary feelings. Below are some
          examples of when to use <i>stare</i> instead of <i>essere</i>
        </p>
        <p>
          Below are the different ways to use <i>stare</i> instead of
          <i> esssere</i>.
        </p>
        <ul>
          <li>
            Stare can also be used to express remaining in place.
            <p>"Oggi, sto in la scuola." --> Today I stay at school</p>
          </li>
          <li>
            Stare can be used to express ones health
            <p>"Come stai?" --> How are you feeling?</p>
          </li>
          <li>
            Stare is used when speaking about someones appearance.
            <p>
              "Questa maglia mi sta buonissimo." --> This shirt looks great on
              me.
            </p>
          </li>
          <p>
            >Stare also has many different idiomatic expressions that it is used
            with. These require memorization as there is no easy rule set to
            remember them by.
          </p>
          <ul>
            <li>Stare in piedi --> to be standing</li>
            <li>Stare attento --> to pay attention</li>
            <li>Stare con... --> to be in a relationship with...</li>
            <li>Stare a cuore --> to have a heart.</li>
          </ul>

          <h5>Let's see if you can recognize which verb to use where.</h5>
          <p>Choose the correct verb, <i>stare</i> or <i> essere</i>.</p>
        </ul>

        <label for="question1">"Oggi, (sto/sono) bene!"</label>
        <input
          :class="{ wrong: answer[0] !== 'sto' }"
          type="text"
          id="question1"
          name="question1"
          v-model.trim="answer[0]"
        />
        <label for="question2">(Siamo/Stiamo) in Germani questa mesa.) </label>
        <input
          :class="{ wrong: answer[1] !== 'siamo' }"
          type="text"
          id="question2"
          name="question2"
          v-model.trim="answer[1]"
        />
        <p></p>
        <label for="question3">"Quanto (sei/stai) alto?"</label>
        <input
          :class="{ wrong: answer[2] !== 'sei' }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[2]"
        />
        <p></p>
        <label for="question4">"Come (sei/stai)?"</label>
        <input
          :class="{ wrong: answer[3] !== 'stai' }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[3]"
        />
        <p></p>
        <label for="question5">"Domani,(sto,sono) a la mia casa."</label>
        <input
          :class="{ wrong: answer[4] !== 'sto' }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[4]"
        />
        <p></p>
        <label for="question6">"Dov'e (siamo,stiamo)adesso?"</label>
        <input
          :class="{ wrong: answer[5] !== 'siamo' }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[5]"
        />
      </div>
    </div>
    <!-- Lesson 4 begins here -->
    <div class="individual-lesson">
      <label for="regular-ar-verbs">Conjugating regular -are verbs </label>
      <button id="regular-ar-verbs" value="ShowLesson4" @click="toggleLesson4">
        Toggle Lesson
      </button>
      <div v-if="toggleL4">
        <h1>Lesson 4: Conjugating regular -are verbs.</h1>
        <p>
          When conjugating verbs that end in -are, most verbs fall into a set
          pattern that can be repeated in order to correctly conjugate each verb
          in each different tense. There are irregular verbs that do not follow
          these rules, but they are rare and must be memorized as there is no
          hard set rule that allows you to conjugate them, but we will address
          those types of verbs in a future lesson.
        </p>
        <p>
          The first stepis to drop the -are ending and replace it with the
          following endings, depending on the which person the verb requires.
        </p>
        <ul>
          <li>-o</li>
          <li>-i</li>
          <li>-a</li>
          <li>-iamo</li>
          <li>-ate</li>
          <li>-ano</li>
        </ul>
        <h5>
          Let's begin by looking at the verb <i>parlare</i> which means to speak
        </h5>

        <p>
          First, let's learn to conjugate the verb <i>parlare</i> so that we can
          see how it is used.
        </p>
        <ul>
          <li>io: {{ parlare.io }} --> I speak</li>
          <li>tu: {{ parlare.tu }} --> You speak</li>
          <li>lui/lei: {{ parlare.lui }} --> He or she speaks</li>
          <li>noi: {{ parlare.noi }} --> We speak</li>
          <li>voi: {{ parlare.voi }} --> You all speak</li>
          <li>loro: {{ parlare.loro }} --> They speak</li>
        </ul>
        <p>
          Now let's look at another -are ending verb<i>mangiare</i> so that we
          can have another example of how the ending of -are verbs are changed
          depending on the useage.
        </p>
        <ul>
          <li>io: {{ mangiare.io }} --> I eat</li>
          <li>tu: {{ mangiare.tu }} --> You eat</li>
          <li>lui/lei: {{ mangiare.lui }} --> He or she eats</li>
          <li>noi: {{ mangiare.noi }} --> We eat</li>
          <li>voi: {{ mangiare.voi }} --> You all eat</li>
          <li>loro: {{ mangiare.loro }} --> They eat</li>
        </ul>

        <h5>Not let's practice conjugating some verbs on your own!</h5>
        <h6>Fill in the correct form of the verb</h6>

        <label for="question1">"I buy (comprare)"</label>
        <input
          :class="{ wrong: answer[0] !== comprare.io }"
          type="text"
          id="question1"
          name="question1"
          v-model.trim="answer[0]"
        />
        <p></p>
        <label for="question2">"We buy"(comprare) </label>
        <input
          :class="{ wrong: answer[1] !== comprare.noi }"
          type="text"
          id="question2"
          name="question2"
          v-model.trim="answer[1]"
        />
        <p></p>
        <label for="question3">"You walk"(Comminare)</label>
        <input
          :class="{ wrong: answer[2] !== comminare.tu }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[2]"
        />
        <p></p>
        <label for="question4">"They walk"(Comminare)</label>
        <input
          :class="{ wrong: answer[3] !== comminare.loro }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[3]"
        />
        <p></p>
        <label for="question5">"You all eat."(mangiare)</label>
        <input
          :class="{ wrong: answer[4] !== mangiare.voi }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[4]"
        />
        <p></p>
        <label for="question6">"I speak"(Parlare)</label>
        <input
          :class="{ wrong: answer[5] !== parlare.io }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[5]"
        />
        <p></p>
        <label for="question7">"You swim"(Nuotare)</label>
        <input
          :class="{ wrong: answer[6] !== nuotare.tu }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[6]"
        />
        <p></p>
        <label for="question8">"She swims"(Nuotare)</label>
        <input
          :class="{ wrong: answer[7] !== nuotare.lui }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[7]"
        />
      </div>
    </div>
    <!-- Lesson 5 begins here -->
    <div class="individual-lesson">
      <label for="regular-ere-verbs">Conjugating regular -ere verbs </label>
      <button id="regular-ere-verbs" value="ShowLesson5" @click="toggleLesson5">
        Toggle Lesson
      </button>
      <div v-if="toggleL5">
        <h1>Lesson 5: Conjugating regular -ere verbs.</h1>
        <p>
          Similar to -are ending verbs, there are many regular -ere ending verbs
          that follow a set pattern that will allow you to conjugate any regular
          -ere verb depending the situation.
        </p>
        <p>
          The first step, same as -are verbs, is to drop the -ere ending and
          replace it with the following endings, depending on which person the
          verb is in.
        </p>
        <ul>
          <li>-o</li>
          <li>-i</li>
          <li>-e</li>
          <li>-iamo</li>
          <li>-ete</li>
          <li>-ono</li>
        </ul>

        <p>
          First, let's practice with the verb <i>credere</i> meaning to
          believe,so that we can see how it looks in action.
        </p>
        <ul>
          <li>io: {{ credere.io }} --> I believe</li>
          <li>tu: {{ credere.tu }} --> You believe</li>
          <li>lui/lei: {{ credere.lui }} --> He or she believes</li>
          <li>noi: {{ credere.noi }} --> We believe</li>
          <li>voi: {{ credere.voi }} --> You believe</li>
          <li>loro: {{ credere.loro }} --> They believe</li>
        </ul>

        <h5>Not let's practice conjugating some verbs on your own!</h5>
        <h6>Fill in the correct form of the verb</h6>

        <label for="question1">"I believe(credere)"</label>
        <input
          :class="{ wrong: answer[0] !== credere.io }"
          type="text"
          id="question1"
          name="question1"
          v-model.trim="answer[0]"
        />
        <p></p>
        <label for="question2">"We believe (credere)" </label>
        <input
          :class="{ wrong: answer[1] !== credere.noi }"
          type="text"
          id="question2"
          name="question2"
          v-model.trim="answer[1]"
        />
        <p></p>
        <label for="question3">They ask(chiedere)</label>
        <input
          :class="{ wrong: answer[2] !== chiedere.loro }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[2]"
        />
        <p></p>
        <label for="question4">I ask (chiedere)</label>
        <input
          :class="{ wrong: answer[3] !== chiedere.io }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[3]"
        />
      </div>
    </div>
    <!-- Lesson 6 begins here -->
    <div class="individual-lesson">
      <label for="regular-ire-verbs">Conjugating regular -ire verbs </label>
      <button id="regular-ire-verbs" value="ShowLesson6" @click="toggleLesson6">
        Toggle Lesson
      </button>
      <div v-if="toggleL6">
        <h1>Lesson 6: Conjugating regular -ire verbs.</h1>
        <p>
          As was similar with the other two versions of verbs in italian, -ire
          ending verbs also follow a similar predictable pattern for the most
          part so let's take a look at how we go about creating the new endings
          of -ire verbs.
        </p>

        <ul>
          <li>-o</li>
          <li>-i</li>
          <li>-e</li>
          <li>-iamo</li>
          <li>-ite</li>
          <li>-ono</li>
        </ul>

        <p>
          First, let's practice with the verb <i>dormire</i> meaning to sleep,so
          that we can see how it looks in action.
        </p>
        <ul>
          <li>io: {{ dormire.io }} --> I sleep</li>
          <li>tu: {{ dormire.tu }} --> You sleep</li>
          <li>lui/lei: {{ dormire.lui }} --> He or she sleeps</li>
          <li>noi: {{ dormire.noi }} --> We sleep</li>
          <li>voi: {{ dormire.voi }} --> You sleep</li>
          <li>loro: {{ dormire.loro }} --> They sleep</li>
        </ul>
        <h5>Not let's practice conjugating some verbs on your own!</h5>
        <h6>Fill in the correct form of the verb</h6>

        <label for="question1">"I sleep (dormire)"</label>
        <input
          :class="{ wrong: answer[0] !== dormire.io }"
          type="text"
          id="question1"
          name="question1"
          v-model.trim="answer[0]"
        />
        <p></p>
        <label for="question2">"We feel (sentire)" </label>
        <input
          :class="{ wrong: answer[1] !== sentire.noi }"
          type="text"
          id="question2"
          name="question2"
          v-model.trim="answer[1]"
        />
        <p></p>
        <label for="question3">They sleep(dormire)</label>
        <input
          :class="{ wrong: answer[2] !== dormire.loro }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[2]"
        />
        <p></p>
        <label for="question4">I hear (sentire)</label>
        <input
          :class="{ wrong: answer[3] !== sentire.io }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[3]"
        />
      </div>
    </div>
    <!-- Lesson 7 begins here -->
    <div class="individual-lesson">
      <label for="irregular-verbs">Conjugating irregular verbs </label>
      <button id="irregular-verbs" value="ShowLesson7" @click="toggleLesson7">
        Toggle Lesson
      </button>
      <div v-if="toggleL7">
        <h1>Lesson 7: Conjugating irregular verbs.</h1>
        <p>
          Outside of the previously mentioned forms of verbs lies another group
          of verbs that don't exactl follow the same rules as the others and
          these are known as irregular verbs, or verbs whos patterns differ from
          the other three groups. Luckily, there tend to be a set of noticeable
          patterns that can help you out, but most just require memorization.
        </p>
        <p>
          Let's begin by looking at one of the more common, irregular patterns
          that we see with the verb <i>capire</i>, meaning to know something.
        </p>
        <ul>
          <li>io: {{ capire.io }} --> I know</li>
          <li>io: {{ capire.tu }} --> you know</li>
          <li>io: {{ capire.lui }} --> he or she knows</li>
          <li>io: {{ capire.noi }} --> we know</li>
          <li>io: {{ capire.voi }} --> you all know</li>
          <li>io: {{ capire.loro }} --> they know</li>
        </ul>
        <p>
          As you can see in the -io form we drop the ending and add 'isco', in
          the -tu form, we drop the ending and add 'isci' while in the third
          person singular form we drop the ending and add 'isce', the noi/voi
          forms follow the old regular pattern, and in the third person plural
          form we again drop the ending and add a new ending of 'iscono'
        </p>
        <p></p>
        <p>
          Now let's look at two verbs that are almost as common as
          <i>essere</i> and <i> stare</i> and those are going to be two
          irregular verbs, <i>fare</i>, meaning to do or to make, and
          <i>andare</i> which means to go. Both of these verbs have their own
          rules for conjugation and therefore require memorization to really get
          them down.
        </p>
        <p></p>
        <h5>Let's begin by taking a look at <i>andare</i></h5>
        <ul>
          <li>io: {{ andare.io }} --> I go</li>
          <li>tu: {{ andare.tu }} --> You go</li>
          <li>lui/lei: {{ andare.lui }} --> He or she goes</li>
          <li>noi: {{ andare.noi }} --> We go</li>
          <li>voi: {{ andare.voi }} --> You all go</li>
          <li>loro: {{ andare.loro }} --> They go</li>
        </ul>
        <h5>Now let's take a look at <i>fare</i></h5>
        <ul>
          <li>io: {{ fare.io }} --> I do</li>
          <li>tu: {{ fare.tu }} --> You do</li>
          <li>lui/lei: {{ fare.lui }} --> He or she does</li>
          <li>noi: {{ fare.noi }} --> We do</li>
          <li>voi: {{ fare.voi }} --> You all do</li>
          <li>loro: {{ fare.loro }} --> They do</li>
        </ul>
        <p>
          As we can see from both of common irregular verbs, there isn't really
          an easy pattern to distinguish them in order to remember the forms
          easily so it's important that for common verbs like this you memorize
          their different uses.
        </p>
        <h5>Not let's practice conjugating some of these verbs on your own!</h5>
        <h6>Fill in the correct form of the verb</h6>

        <label for="question1">"I know (capire)"</label>
        <input
          :class="{ wrong: answer[0] !== capire.io }"
          type="text"
          id="question1"
          name="question1"
          v-model.trim="answer[0]"
        />
        <p></p>
        <label for="question2">"We do/make (fare)" </label>
        <input
          :class="{ wrong: answer[1] !== fare.noi }"
          type="text"
          id="question2"
          name="question2"
          v-model.trim="answer[1]"
        />
        <p></p>
        <label for="question3">They go(andare)</label>
        <input
          :class="{ wrong: answer[2] !== andare.loro }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[2]"
        />
        <p></p>
        <label for="question4">She knows (capire)</label>
        <input
          :class="{ wrong: answer[3] !== capire.lui }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[3]"
        />
        <p></p>
        <label for="question4">We go (andare)</label>
        <input
          :class="{ wrong: answer[4] !== andare.noi }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[4]"
        />
        <p></p>
        <label for="question4">I make (fare))</label>
        <input
          :class="{ wrong: answer[5] !== fare.io }"
          type="text"
          id="question4"
          name="question4"
          v-model.trim="answer[5]"
        />
      </div>
    </div>
    <!-- Lesson 8 begins here -->
    <div class="individual-lesson">
      <label for="pronouns">Italian Pronouns</label>
      <button id="pronouns" value="ShowLesson8" @click="toggleLesson8">
        Toggle Lesson
      </button>
      <div v-if="toggleL8">
        <h1>Lesson 8: Italian pronouns</h1>
        <p></p>
        <p>
          Now let's look at two verbs that are almost as common as
          <i>essere</i> and <i> stare</i> and those are going to be two
          irregular verbs, <i>fare</i>, meaning to do or to make, and
          <i>andare</i> which means to go. Both of these verbs have their own
          rules for conjugation and therefore require memorization to really get
          them down.
        </p>
        <p></p>
        <h5>Let's begin by taking a look at <i>andare</i></h5>
        <ul>
          <li>First person singular: io --> I</li>
          <li>Second person singular: tu --> you</li>
          <li>Third person singular masculine: lui --> he</li>
          <li>Third person singular feminine: lei --> she</li>
          <li>First personal plural: noi --> we</li>
          <li>Second person plural: voi --> you all</li>
          <li>Third person plural: loro -- They</li>
        </ul>

        <p>
          Now if you look at the third person singular you can see that there
          are two different forms it can take, one being the masculine and one
          being the feminine. This is an important concept in italian as words
          can take one of two genders, male or female, which alters how the
          words interact with auxiliary words around them. We will go into more
          detail about this in a future lesson but for now its just important to
          know that a word can be either masculine, or feminine.
        </p>
        <p></p>
        <p>
          An interesting part of the italian language pronoun use is that in
          most cases, when the subject is assumed, you can omit even using the
          pronouns before the word they can become almost like an additional
          point of detail about a subject in the event that it is unclear.
        </p>
        <p></p>
        <p>
          One other important concept to note about pronouns, is that the third
          person singular forms (lei/lui) can be used in exchange of the second
          person singular(tu) when speaking to someone formally in order to show
          respect.
        </p>

        <p></p>
        <p>
          There's not much to practice for this lesson, it is just important to
          know what the italian pronouns are and where they are used in order to
          build a strong foundation to your learning.
        </p>
      </div>
    </div>
    <!-- Lesson 9 begins here -->
    <div class="individual-lesson">
      <label for="direct-object-pronouns">Italian direct object pronouns</label>
      <button
        id="direct-object-pronouns"
        value="ShowLesson9"
        @click="toggleLesson9"
      >
        Toggle Lesson
      </button>
      <div v-if="toggleL9">
        <h1>Lesson 9: Italian direct object pronouns</h1>
        <p></p>
        <p>First, what is a direct object pronoun?</p>
        <p>
          a direct object pronoun is used to indicate who the direct recipient
          of an action is, and then replaces the object noun( a person place or
          thing).
        </p>
        <p></p>
        <h5>
          Let's begin by taking a look at the italian direct object pronouns
        </h5>
        <ul>
          <li>First person singular: mi --> me</li>
          <li>Second person singular: ti --> you</li>
          <li>Third person singular masculine: lo --> him/it</li>
          <li>Third person singular feminine: la --> she/it</li>
          <li>First personal plural: ci --> us/li></li>
          <li>Second person plural: vi --> you</li>
          <li>Third person plural: loro -- Them</li>
        </ul>

        <p>
          Similar to the pronouns we learned about earlier, if you look at the
          singular third person you can see two different forms, one referring
          to the masculine singular, and another to the feminine singular, it is
          again important that you notice the difference between the two forms
          because it is an important concept later in the lessons.
        </p>
        <p></p>
        <h5>
          Now let's look at a couple examples of direct object pronouns in
          action, so we can see how they work!
        </h5>
        <ul>
          <li>
            Frederico va alla scuola. --> Frederico la va.
            <p>
              Frederico goes to the school. --> <i>Frederico goes there.</i>
            </p>
          </li>
          <li>
            Margarita beve il vino --> Margarita lo beve
            <p>Margarita drinks the wine. --> <i>Margarita drinks it.</i></p>
          </li>
          <li>
            Paulo mangia il pane. --> Paulo lo mangia.
            <p>Paulo eats the bread --> <i>Paulo eats it.</i></p>
          </li>
        </ul>
        <h5>
          Now that you have seen how direct object pronouns work, let's practice
          a few on our own!
        </h5>
        <h6>
          Select the correct direct object pronoun that replaces the object noun
          in the sentence.
        </h6>
        <label for="question1">Io mangio la pizza ---> io __ mangia.</label>
        <input
          :class="{ wrong: answer[0] !== 'la' }"
          type="text"
          id="question1"
          name="question1"
          v-model.trim="answer[0]"
        />
        <p></p>
        <label for="question2">Io faccio la torta. --> io __ faccio. </label>
        <input
          :class="{ wrong: answer[1] !== 'la' }"
          type="text"
          id="question2"
          name="question2"
          v-model.trim="answer[1]"
        />
        <p></p>
        <label for="question3">Tu e i ragazzi sedete --> sedete__</label>
        <input
          :class="{ wrong: answer[2] !== 'vi' }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[2]"
        />
        <p></p>
      </div>
    </div>
    <!-- lesson 10 begins here -->
    <div class="individual-lesson">
      <label for="indirect-object-pronouns"
        >Italian indirect object pronouns</label
      >
      <button
        id="indirect-object-pronouns"
        value="ShowLesson10"
        @click="toggleLesson10"
      >
        Toggle Lesson
      </button>
      <div v-if="toggleL10">
        <h1>Lesson 10: Italian indirect object pronouns</h1>
        <p></p>
        <p>First, what is an indirect object pronoun?</p>
        <p>
          an indirect object pronoun is used to indicate to whom or to what.
        </p>
        <p></p>
        <h5>
          Let's begin by taking a look at the italian indirect object pronouns
        </h5>
        <ul>
          <li>First person singular: mi --> me</li>
          <li>Second person singular: ti --> you</li>
          <li>Third person singular masculine: gli --> him/it</li>
          <li>Third person singular feminine: le --> her/it</li>
          <li>First personal plural: ci --> us/li></li>
          <li>Second person plural: vi --> you</li>
          <li>Third person plural: loro/gli -- Them</li>
        </ul>

        <p>
          The easiest way to think about indirect object pronouns is to ask
          yourself the question "to what?",or "to whom?" is the verb or action
          in question referring to.
        </p>
        <p></p>
        <h5>
          Now let's look at a couple examples of indirect object pronouns in
          action, so we can see how they work!
        </h5>
        <ul>
          <li>
            Frederico cammina verso ai ragazzi. --> Frederico walks towards the
            kids.
            <p>
              Frederico loro verso cammina. -->
              <i>Frederico walks towards them.</i>
            </p>
          </li>
          <li>
            Margarita vede Francesco --> Margarita lo vede
            <p>Margarita sees Francesco --> <i>Margarita sees him.</i></p>
          </li>
          <li>
            Paulo mangia con me e Louisa --> Paulo con ci mangia.
            <p>Paulo eats with me and Louisa --> <i>Paulo eats with us.</i></p>
          </li>
        </ul>
        <h5>
          Now that you have seen how indirect object pronouns work, let's
          practice a few on our own!
        </h5>
        <h6>
          Select the correct indirect object pronoun that replaces the subject
          in the sentence.
        </h6>
        <label for="question1"
          >Io mangio con Laura e Paulo ---> io con __ mangia.</label
        >
        <input
          :class="{ wrong: answer[0] !== 'loro' }"
          type="text"
          id="question1"
          name="question1"
          v-model.trim="answer[0]"
        />
        <p></p>
        <label for="question2"
          >io prendo il gatto a Paulo --> io __ prendo il gatto
        </label>
        <input
          :class="{ wrong: answer[1] !== 'gli' }"
          type="text"
          id="question2"
          name="question2"
          v-model.trim="answer[1]"
        />
        <p></p>
        <label for="question3"
          >Io compro Francesca una tavola. --> Io __ compro una tavola.</label
        >
        <input
          :class="{ wrong: answer[2] !== 'le' }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[2]"
        />
        <p></p>
        <label for="question3"
          >Io chiedo la professoressa una domanda. --> io __ chiedo una
          domanda.</label
        >
        <input
          :class="{ wrong: answer[3] !== 'le' }"
          type="text"
          id="question3"
          name="question3"
          v-model.trim="answer[3]"
        />
        <p></p>
      </div>
    </div>
  </div>
  <div v-else>
    <div class="text-center">
      <SetUserName />
    </div>
  </div>
</template>
<script>
import axios from "axios";
import SetUserName from "../components/General/SetUserName.vue";
export default {
  components: {
    SetUserName,
  },
  data() {
    return {
      answer1: null,
      answer2: null,
      answer3: null,
      answer4: null,
      answer5: null,
      answer6: null,
      user: {
          email: "asdf"
      },
      avere: {
        io: "ho",
        tu: "hai",
        lui: "ha",
        noi: "abbiamo",
        voi: "avete",
        loro: "hanno",
      },
      essere: {
        io: "sono",
        tu: "sei",
        lui: "e",
        noi: "siamo",
        voi: "siete",
        loro: "sono",
      },
      stare: {
        io: "sto",
        tu: "stai",
        lui: "sta",
        noi: "stiamo",
        voi: "state",
        loro: "stanno",
      },
      parlare: {
        io: "parlo",
        tu: "parli",
        lui: "parla",
        noi: "parliamo",
        voi: "parlate",
        loro: "parlano",
      },
      mangiare: {
        io: "mangio",
        tu: "mangi",
        lui: "mangia",
        noi: "mangiamo",
        voi: "mangiate",
        loro: "mangiano",
      },
      comprare: {
        io: "compro",
        tu: "compri",
        lui: "compra",
        noi: "compriamo",
        voi: "compriate",
        loro: "comprano",
      },
      comminare: {
        io: "commino",
        tu: "commini",
        lui: "commina",
        noi: "comminiamo",
        voi: "comminiate",
        loro: "comminano",
      },
      nuotare: {
        io: "nuoto",
        tu: "nuoti",
        lui: "nuota",
        noi: "nuotiamo",
        voi: "nuotiate",
        loro: "nuotano",
      },
      credere: {
        io: "credo",
        tu: "credi",
        lui: "crede",
        noi: "crediamo",
        voi: "credete",
        loro: "credono",
      },
      chiedere: {
        io: "chiedo",
        tu: "chiedi",
        lui: "chiede",
        noi: "chiediamo",
        voi: "chiedete",
        loro: "chiedono",
      },
      dormire: {
        io: "dormo",
        tu: "dormi",
        lui: "dorme",
        noi: "dormiamo",
        voi: "dormite",
        loro: "dormono",
      },
      sentire: {
        io: "sento",
        tu: "senti",
        lui: "sente",
        noi: "sentiamo",
        voi: "sentite",
        loro: "sentono",
      },
      capire: {
        io: "capisco",
        tu: "capisci",
        lui: "capisce",
        noi: "capiamo",
        voi: "capite",
        loro: "capiscono",
      },
      andare: {
        io: "vado",
        tu: "vai",
        lui: "va",
        noi: "andiamo",
        voi: "andate",
        loro: "vanno",
      },
      fare: {
        io: "faccio",
        tu: "fai",
        lui: "fa",
        noi: "facciamo",
        voi: "fate",
        loro: "fanno",
      },

      answer: [],
      toggleL1: false,
      toggleL2: false,
      toggleL3: false,
      toggleL4: false,
      toggleL5: false,
      toggleL6: false,
      toggleL7: false,
      toggleL8: false,
      toggleL9: false,
      toggleL10: false,
    };
  },
  watch: {
    answer1: function (val) {
      if (val === "abbiamo") {
        this.processing = true;
        axios
          .patch("/api/users/" + this.$auth.user.email)
          .then(() => {
            this.processing = false;
          })
          .catch(() => {
            this.processing = false;
          });
      }
    },
  },
  mounted() {
    this.updateCurrentUser(this.$auth.user.email);
  },
  methods: {
    updateCurrentUser(email) {
      this.processing = true;
      axios
        .get("/api/users/" + email)
        .then((response) => {
          this.processing = false;
          this.user = response.data;
        })
        .catch(() => {
          this.processing = false;
        });
    },
    toggleLesson1() {
      this.toggleL1 = !this.toggleL1;
      // alert(this.toggleL1[0]);
    },
    toggleLesson2() {
      this.toggleL2 = !this.toggleL2;
    },
    toggleLesson3() {
      this.toggleL3 = !this.toggleL3;
    },
    toggleLesson4() {
      this.toggleL4 = !this.toggleL4;
    },
    toggleLesson5() {
      this.toggleL5 = !this.toggleL5;
    },
    toggleLesson6() {
      this.toggleL6 = !this.toggleL6;
    },
    toggleLesson7() {
      this.toggleL7 = !this.toggleL7;
    },
    toggleLesson8() {
      this.toggleL8 = !this.toggleL8;
    },
    toggleLesson9() {
      this.toggleL9 = !this.toggleL9;
    },
    toggleLesson10() {
      this.toggleL10 = !this.toggleL10;
    },
  },
};
</script>

<style scoped>
.individual-lesson {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  margin: 2rem auto;
  max-width: 40rem;
}
div header {
  color: #fff;
  padding-top: 5vw;
  padding-bottom: 5vw;
  background-color: #03205f;
  text-align: center;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  text-transform: uppercase;
  max-width: 40rem;
  margin: auto;
}
div input {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  margin: 2rem auto;
  max-width: 40rem;
}
.wrong {
  border-color: red;
  border-radius: 20px;
}
div button {
  margin-left: 75%;
  padding: 1rem;
}
div label {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  margin: 1rem auto;
  max-width: 40rem;
  color: white;
  background-color: #03205f;
}
button {
  padding: 0.5em 3em;
  border: 0.16em solid #ffffff;
  margin: 0 0.3em 0.3em 0;
  box-sizing: border-box;
  text-decoration: none;
  text-transform: uppercase;
  font-family: "Roboto", sans-serif;
  font-weight: 400;
  color: white;
  background-color: #03205f;
  text-align: center;
  transition: all 0.25s;
}
button:hover {
  background-color: #2c6df8;
  border-color: #dddddd;
}
button:activate {
  color: #03205f;
  border-color: #bbbbbb;
}
@media all and (max-width: 30em) {
  button {
    display: block;
    margin: 0.4em auto;
  }
}
</style>