# Databricks notebook source
service_credential = "fDY8Q~G0DiBNL8M_uVR_FPK0IVUE.bugZy~YBaF-"

spark.conf.set("fs.azure.account.auth.type.tybuldatalakedemo.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.tybuldatalakedemo.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.tybuldatalakedemo.dfs.core.windows.net", "59a63017-a581-4651-ba0f-fe18b30e9b8e")
spark.conf.set("fs.azure.account.oauth2.client.secret.tybuldatalakedemo.dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.tybuldatalakedemo.dfs.core.windows.net", "https://login.microsoftonline.com/94032769-6d65-484f-842f-09d05b51c9ad/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls("abfss://raw@tybuldatalakedemo.dfs.core.windows.net"))
