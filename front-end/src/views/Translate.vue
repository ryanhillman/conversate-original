<template>
  <div class="text-center">
    <div v-if="user">
      <div class="card-style">
        <h2><i>Translate</i></h2>
        <p>
          <b>
            Select a input language, output language, and type or record your
            text to have translated. Once translated click the speaker to hear
            the pronunciation of your translated text.
          </b>
        </p>
      </div>
      <div class="back-card">
        <div class="m-3">
          <label for="selectInputLanguage">Select Input Language</label>
          <br />
          <select
            v-model="inputLanguage"
            name="selectInputLanguage"
            class="form-select"
            aria-label="Select input language"
          >
            <option
              v-bind:key="language.code"
              v-for="language in languages"
              :value="language.code"
              :selected="inputLanguage == language.code"
            >
              {{ language.name }}
            </option>
          </select>
        </div>
        <div class="m-3">
          <label for="selectOutputLanguage">Select Output Language</label>
          <br />
          <select
            v-model="outputLanguage"
            name="selectOutputLanguage"
            class="form-select"
            aria-label="Select output language"
          >
            <option
              v-bind:key="language.code"
              v-for="language in languages"
              :value="language.code"
              :selected="outputLanguage == language.code"
            >
              {{ language.name }}
            </option>
          </select>
        </div>
        <div>
          <textarea
            class="m-2"
            type="text"
            cols="50"
            rows="10"
            style="resize: none"
            v-model="textToTranslate"
          >
          </textarea>
          <div class="m-3">
            <font-awesome-icon
              @click="startSpeechToTxt"
              class="fa-3x m-2"
              :class="recording ? 'text-danger' : ''"
              icon="microphone"
            />
            <font-awesome-icon
              v-if="translatedText"
              @click="startTxtToSpeech"
              class="fa-3x m-2"
              icon="volume-up"
            />
          </div>
          <textarea
            class="m-2"
            disabled
            v-model="translatedText"
            cols="50"
            rows="10"
            style="resize: none"
          ></textarea>
        </div>
        <br />
        <button
          :disabled="
            inputLanguage == null ||
            outputLanguage == null ||
            textToTranslate.length < 1
          "
          class="btn btn-secondary m-3"
          @click="translateEnteredText()"
        >
          Translate
        </button>
      </div>
    </div>
    <div v-else>
        <SetUserName />
      </div>
  </div>
</template>
<script>
import axios from "axios";
import translate from "translate";
import SetUserName from "../components/General/SetUserName.vue";
export default {
  name: "Translate",
  components: {
    SetUserName,
  },
  data() {
    return {
      recording: false,
      textToTranslate: "",
      user: null,
      processing: false,
      translatedText: null,
      inputLanguage: null,
      outputLanguage: null,
      runtimeTranscription_: "",
      transcription_: [],
      languages: [
        { code: "en", name: "English", nativeName: "English" },
        { code: "it", name: "Italian", nativeName: "Italiano" },
      ],
    };
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
    async translateEnteredText() {
      const text = await translate(this.textToTranslate, {
        to: this.outputLanguage,
        from: this.inputLanguage,
      });
      this.translatedText = text;
    },
    startSpeechToTxt() {
      // initialisation of voicereco
      this.recording = true;
      window.SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;
      const recognition = new window.SpeechRecognition();
      recognition.lang = this.inputLanguage;
      recognition.interimResults = true;

      // event current voice reco word
      recognition.addEventListener("result", (event) => {
        var text = Array.from(event.results)
          .map((result) => result[0])
          .map((result) => result.transcript)
          .join("");
        this.runtimeTranscription_ = text;
      });
      // end of transcription
      recognition.addEventListener("end", () => {
        this.transcription_.push(this.runtimeTranscription_);
        this.textToTranslate = this.runtimeTranscription_;
        this.runtimeTranscription_ = "";
        recognition.stop();
        this.recording = false;
      });
      recognition.start();
    },
    startTxtToSpeech() {
      // start speech to txt
      var utterance = new SpeechSynthesisUtterance(this.translatedText);
      utterance.lang = this.outputLanguage;
      window.speechSynthesis.speak(utterance);
    },
  },
  computed: {},
};
</script>
<style lang="scss" scoped>
#btn-new {
  background-color: #2a3f54;
}
.card-style {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  margin: 2rem auto;
  max-width: 40rem;
  color: white;
  background-color: #152f68;
  font-family: "Roboto", sans-serif;
  font-weight: 400;
}
.back-card {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  margin: 2rem auto;
  max-width: 40rem;
  color: white;
  background-color: #c0c0c0;
  font-family: "Roboto", sans-serif;
  font-weight: 400;
}
</style>