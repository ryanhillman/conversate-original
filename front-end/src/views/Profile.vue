<template>
  <div class="container">
    <div class="row align-items-center profile-header">
      <div class="col-md-2 mb-3">
        <img
          :src="$auth.user.picture"
          alt="User's profile picture"
          class="rounded-circle img-fluid profile-picture"
        />
      </div>
      <div class="col-md text-center text-md-left">
          <div v-if="!user">
            <h2>{{ $auth.user.name }}</h2>
            <h3>Has not set a username yet.</h3>
          </div>
          <div v-else>  
              <h1>Stats for: {{ user.user_name }}</h1>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "profile",
  components: {
      
  },
  data() {
    return {
        user: null,
        processing: false
    };
  },
  mounted() {
      this.updateCurrentUser(this.$auth.user.email);
  },
  methods: {
    updateCurrentUser(email){
        this.processing = true;
      axios
        .get("/api/users/" + email)
        .then((response) => {
          this.processing = false
          this.user = response.data;
        }).catch(() => {
          this.processing = false;
        });
    }
  },
};
</script>
