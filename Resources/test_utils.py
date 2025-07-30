# Databricks notebook source
def check_new_year(actual):
    expected = 2025
    if actual == expected:
        display("✅ Correct!")
    else:
        display(f"❌ Incorrect. Your answer: {actual}, Expected: {expected}")