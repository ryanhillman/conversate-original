<template>
  <div class="text-center hero">
    <h1 class="mb-4"><template>
        <div id="app">
        </div>
      </template>
    </h1>
    <div class="card-style">
      <h1><i>Welcome to Conversate!</i></h1>
      <p>
        <b>One site, every aspect of learning Italian!</b>
      </p>
      <!--<p v-if="$auth.isAuthenticated" class="nav-item">
              <router-link to="/Lesson" class="nav-link">Lessons</router-link>
            </p> -->
    </div>
    <div class="cards">
      <form>
  <div class="card" style="width: 18rem;">
  <img class="card-img-top" src="study.png" alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">Learn!</h5>
    <p class="card-text">Practice with Italian lessons!</p>
    <a href="/lesson" class="btn btn-primary">Lessons</a>
  </div>
</div>
  </form>
  <form>
<div class="card" style="width: 18rem;">
  <img class="card-img-top" src="translate.png" alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">Translate!</h5>
    <p class="card-text">Use our translation feature to translate from text-to-speech and speech-to-text!</p>
    <a href="/translate" class="btn btn-primary">Translate</a>
  </div>
</div>
  </form>
  <form>
<div class="card" style="width: 18rem;">
  <img class="card-img-top" src="check.png" alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">Mastery!</h5>
    <p class="card-text">View your progress and gauge your improvement in italian!</p>
    <a href="/dashboard" class="btn btn-primary">Mastery</a>
  </div>
</div>
  </form>
  </div>
  </div>
</template>

<script>
export default {
  name: "Hero"
};
</script>
<style scoped>
.card-style{
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0, 0, 0, 0.26);
    padding: 1rem;
    margin:2rem auto;
    max-width:40rem;
    color:white;
    background-color:#152f68;
    font-family:'Roboto',sans-serif;
    font-weight:400;
}
.cards{
  display:flex;
  margin-left: auto;
  margin-right: auto;
  justify-content: center;
  padding: 2rem;
  }
.cards form{
  margin-left: 1rem;
  margin-right: 1rem;
}
.card{
  height: 30rem;
  border-radius:12px;
  box-shadow:0 2px 8px rgba(0, 0, 0, 0.26);
}

</style>
