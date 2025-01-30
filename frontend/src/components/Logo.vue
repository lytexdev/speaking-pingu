<template>
    <div class="logo">
        <img class="logo-image" :src="logoUrl" alt="Speaking-Pingu Logo" height="64px" width="64px">
        <h1>{{ title }}</h1>
    </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
    title: String
})
const logoUrl = '/static/logo.svg'
</script>
