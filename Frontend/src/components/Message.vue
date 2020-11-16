<template>
  <div class="box is-info">
    <p>
      <slot></slot>
    </p>
  </div>
</template>

<script>
export default {};
</script>

<style>
.box {
  background: gray;
  padding: 1px;
  border: 1px solid black;
}
</style>
