# -*- coding: utf-8 -*-
#
# libocispec - a C library for parsing OCI spec files.
#
# Copyright (C) Huawei Technologies., Ltd. 2018-2020.
# Copyright (C) 2017, 2019 Giuseppe Scrivano <giuseppe@scrivano.org>
#
# libocispec is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# libocispec is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with libocispec.  If not, see <http://www.gnu.org/licenses/>.

# As a special exception, you may create a larger work that contains
# part or all of the libocispec parser skeleton and distribute that work
# under terms of your choice, so long as that work isn't itself a
# parser generator using the skeleton or a modified version thereof
# as a parser skeleton.  Alternatively, if you modify or redistribute
# the parser skeleton itself, you may (at your option) remove this
# special exception, which will cause the skeleton and the resulting
# libocispec output files to be licensed under the GNU General Public
# License without this special exception.

import os
import fcntl

"""
Description: json common c code
Interface: None
History: 2019-06-18
Purpose: defined the common tool function for parse json
Defined the CODE global variable to hold the c code
"""
def generate_json_common_c(out):
    with open(os.path.join(out, 'json_common.c'), "w") as source_file:
        fcntl.flock(source_file, fcntl.LOCK_EX)
        source_file.write("""// Auto generated file. Do not edit!
# define _GNU_SOURCE
# include <stdio.h>
# include <string.h>
# include <errno.h>
# include <limits.h>
# include "json_common.h"

#define YAJL_GET_OBJECT_NO_CHECK(v) (&(v)->u.object)
#define YAJL_GET_STRING_NO_CHECK(v) ((v)->u.string)

# define MAX_NUM_STR_LEN 21

static yajl_gen_status gen_yajl_val (yajl_val obj, yajl_gen g, parser_error *err);

static yajl_gen_status gen_yajl_val_obj (yajl_val obj, yajl_gen g, parser_error *err)
{
    size_t i;
    yajl_gen_status stat = yajl_gen_status_ok;

    stat = yajl_gen_map_open (g);
    if (yajl_gen_status_ok != stat)
        GEN_SET_ERROR_AND_RETURN (stat, err);

    for (i = 0; i < obj->u.object.len; i++)
    {
        stat = yajl_gen_string (g, (const unsigned char *) obj->u.object.keys[i], strlen (obj->u.object.keys[i]));
        if (yajl_gen_status_ok != stat)
            GEN_SET_ERROR_AND_RETURN (stat, err);
        stat = gen_yajl_val (obj->u.object.values[i], g, err);
        if (yajl_gen_status_ok != stat)
            GEN_SET_ERROR_AND_RETURN (stat, err);
    }

    stat = yajl_gen_map_close (g);
    if (yajl_gen_status_ok != stat)
        GEN_SET_ERROR_AND_RETURN (stat, err);
    return yajl_gen_status_ok;
}

static yajl_gen_status gen_yajl_val_array (yajl_val arr, yajl_gen g, parser_error *err)
{
    size_t i;
    yajl_gen_status stat = yajl_gen_status_ok;

    stat = yajl_gen_array_open (g);
    if (yajl_gen_status_ok != stat)
        GEN_SET_ERROR_AND_RETURN (stat, err);

    for (i = 0; i < arr->u.array.len; i++)
    {
        stat = gen_yajl_val (arr->u.array.values[i], g, err);
        if (yajl_gen_status_ok != stat)
            GEN_SET_ERROR_AND_RETURN (stat, err);
    }

    stat = yajl_gen_array_close (g);
    if (yajl_gen_status_ok != stat)
        GEN_SET_ERROR_AND_RETURN (stat, err);
    return yajl_gen_status_ok;
}

static yajl_gen_status gen_yajl_val (yajl_val obj, yajl_gen g, parser_error *err)
{
    yajl_gen_status __stat = yajl_gen_status_ok;
    char *__tstr;

    switch(obj->type)
    {
        case yajl_t_string:
            __tstr = YAJL_GET_STRING (obj);
            if (__tstr == NULL) {
                return __stat;
            }
            __stat = yajl_gen_string (g, (const unsigned char *) __tstr, strlen (__tstr));
            GEN_SET_ERROR_AND_RETURN (__stat, err);
        case yajl_t_number:
            __tstr = YAJL_GET_NUMBER (obj);
            if (__tstr == NULL) {
                return __stat;
            }
            __stat = yajl_gen_number (g, __tstr, strlen (__tstr));
            GEN_SET_ERROR_AND_RETURN (__stat, err);
        case yajl_t_object:
            return gen_yajl_val_obj (obj, g, err);
        case yajl_t_array:
            return gen_yajl_val_array (obj, g, err);
        case yajl_t_true:
            return yajl_gen_bool (g, true);
        case yajl_t_false:
            return yajl_gen_bool (g, false);
        case yajl_t_null:
        case yajl_t_any:
            return __stat;
    }
    return __stat;
}

yajl_gen_status gen_yajl_object_residual (yajl_val obj, yajl_gen g, parser_error *err)
{
    size_t i;
    yajl_gen_status stat = yajl_gen_status_ok;

    for (i = 0; i < obj->u.object.len; i++)
    {
        if (obj->u.object.keys[i] == NULL)
        {
            continue;
        }
        stat = yajl_gen_string (g, (const unsigned char *) obj->u.object.keys[i], strlen (obj->u.object.keys[i]));
        if (yajl_gen_status_ok != stat)
            GEN_SET_ERROR_AND_RETURN (stat, err);
        stat = gen_yajl_val (obj->u.object.values[i], g, err);
        if (yajl_gen_status_ok != stat)
            GEN_SET_ERROR_AND_RETURN (stat, err);
    }

    return yajl_gen_status_ok;
}

yajl_gen_status
map_uint (void *ctx, long long unsigned int num)
{
  char numstr[MAX_NUM_STR_LEN];
  int ret;

  ret = snprintf (numstr, sizeof (numstr), "%llu", num);
  if (ret < 0 || (size_t) ret >= sizeof (numstr))
    return yajl_gen_in_error_state;
  return yajl_gen_number ((yajl_gen) ctx, (const char *) numstr,
			  strlen (numstr));
}

yajl_gen_status
map_int (void *ctx, long long int num)
{
  char numstr[MAX_NUM_STR_LEN];
  int ret;

  ret = snprintf (numstr, sizeof (numstr), "%lld", num);
  if (ret < 0 || (size_t) ret >= sizeof (numstr))
    return yajl_gen_in_error_state;
  return yajl_gen_number ((yajl_gen) ctx, (const char *) numstr,
			  strlen (numstr));
}


bool
json_gen_init (yajl_gen * g, const struct parser_context *ctx)
{
  *g = yajl_gen_alloc (NULL);
  if (NULL == *g)
    return false;

  yajl_gen_config (*g, yajl_gen_beautify,
		   (int) (!(ctx->options & OPT_GEN_SIMPLIFY)));
  yajl_gen_config (*g, yajl_gen_validate_utf8,
		   (int) (!(ctx->options & OPT_GEN_NO_VALIDATE_UTF8)));
  return true;
}

yajl_val
get_val (yajl_val tree, const char *name, yajl_type type)
{
  const char *path[] = { name, NULL };
  return yajl_tree_get (tree, path, type);
}

int
common_safe_double (const char *numstr, double *converted)
{
  char *err_str = NULL;
  double d;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  d = strtod (numstr, &err_str);
  if (errno > 0)
    return -errno;


  if (err_str == NULL || err_str == numstr || *err_str != '\\0')
    return -EINVAL;

  *converted = d;
  return 0;
}

int
common_safe_uint8 (const char *numstr, uint8_t * converted)
{
  char *err = NULL;
  unsigned long int uli;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  uli = strtoul (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  if (uli > UINT8_MAX)
    return -ERANGE;

  *converted = (uint8_t) uli;
  return 0;
}

int
common_safe_uint16 (const char *numstr, uint16_t * converted)
{
  char *err = NULL;
  unsigned long int uli;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  uli = strtoul (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  if (uli > UINT16_MAX)
    return -ERANGE;

  *converted = (uint16_t) uli;
  return 0;
}

int
common_safe_uint32 (const char *numstr, uint32_t * converted)
{
  char *err = NULL;
  unsigned long long int ull;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  ull = strtoull (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  if (ull > UINT32_MAX)
    return -ERANGE;

  *converted = (uint32_t) ull;
  return 0;
}

int
common_safe_uint64 (const char *numstr, uint64_t * converted)
{
  char *err = NULL;
  unsigned long long int ull;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  ull = strtoull (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  *converted = (uint64_t) ull;
  return 0;
}

int
common_safe_uint (const char *numstr, unsigned int *converted)
{
  char *err = NULL;
  unsigned long long int ull;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  ull = strtoull (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  if (ull > UINT_MAX)
    return -ERANGE;

  *converted = (unsigned int) ull;
  return 0;
}

int
common_safe_int8 (const char *numstr, int8_t * converted)
{
  char *err = NULL;
  long int li;

  if (numstr == NULL)
    {
      return -EINVAL;
    }

  errno = 0;
  li = strtol (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  if (li > INT8_MAX || li < INT8_MIN)
    return -ERANGE;

  *converted = (int8_t) li;
  return 0;
}

int
common_safe_int16 (const char *numstr, int16_t * converted)
{
  char *err = NULL;
  long int li;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  li = strtol (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  if (li > INT16_MAX || li < INT16_MIN)
    return -ERANGE;

  *converted = (int16_t) li;
  return 0;
}

int
common_safe_int32 (const char *numstr, int32_t * converted)
{
  char *err = NULL;
  long long int lli;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  lli = strtol (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  if (lli > INT32_MAX || lli < INT32_MIN)

    return -ERANGE;

  *converted = (int32_t) lli;
  return 0;
}

int
common_safe_int64 (const char *numstr, int64_t * converted)
{
  char *err = NULL;
  long long int lli;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  lli = strtoll (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  *converted = (int64_t) lli;
  return 0;
}

int
common_safe_int (const char *numstr, int *converted)
{
  char *err = NULL;
  long long int lli;

  if (numstr == NULL)
    return -EINVAL;

  errno = 0;
  lli = strtol (numstr, &err, 0);
  if (errno > 0)
    return -errno;

  if (err == NULL || err == numstr || *err != '\\0')
    return -EINVAL;

  if (lli > INT_MAX || lli < INT_MIN)
    return -ERANGE;

  *converted = (int) lli;
  return 0;
}

yajl_gen_status
gen_json_map_int_int (void *ctx, const json_map_int_int * map,
		      const struct parser_context *ptx, parser_error * err)
{
  yajl_gen_status stat = yajl_gen_status_ok;
  yajl_gen g = (yajl_gen) ctx;
  size_t len = 0, i = 0;
  if (map != NULL)
    len = map->len;
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 0);
  stat = yajl_gen_map_open ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  for (i = 0; i < len; i++)
    {
      char numstr[MAX_NUM_STR_LEN];
      int nret;
      nret =
	snprintf (numstr, sizeof (numstr), "%lld",
		  (long long int) map->keys[i]);
      if (nret < 0 || (size_t) nret >= sizeof (numstr))
	{
	  if (!*err && asprintf (err, "Error to print string") < 0)
	    *(err) = strdup ("error allocating memory");
	  return yajl_gen_in_error_state;
	}
      stat =
	yajl_gen_string ((yajl_gen) g, (const unsigned char *) numstr,
			 strlen (numstr));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
      stat = map_int (g, map->values[i]);
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
    }

  stat = yajl_gen_map_close ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 1);
  return yajl_gen_status_ok;
}

void
free_json_map_int_int (json_map_int_int * map)
{
  if (map != NULL)
    {
      free (map->keys);
      map->keys = NULL;
      free (map->values);
      map->values = NULL;
      free (map);
    }
}

json_map_int_int *
make_json_map_int_int (yajl_val src, const struct parser_context *ctx,
		       parser_error * err)
{
  json_map_int_int *ret = NULL;
  size_t i;
  size_t len;

  (void) ctx;			/* Silence compiler warning.  */

  if (src == NULL || YAJL_GET_OBJECT (src) == NULL)
    return NULL;

  len = YAJL_GET_OBJECT_NO_CHECK (src)->len;
  ret = calloc (1, sizeof (*ret));
  if (ret == NULL)
    return NULL;

  ret->len = 0;
  ret->keys = calloc (len + 1, sizeof (int));
  if (ret->keys == NULL)
    {
      free (ret);
      return NULL;
    }

  ret->values = calloc (len + 1, sizeof (int));
  if (ret->values == NULL)
    {
      free (ret->keys);
      free (ret);
      return NULL;
    }

  for (i = 0; i < len; i++)
    {
      const char *srckey = YAJL_GET_OBJECT_NO_CHECK (src)->keys[i];
      yajl_val srcval = YAJL_GET_OBJECT_NO_CHECK (src)->values[i];

      ret->keys[i] = 0;
      ret->values[i] = 0;
      ret->len = i + 1;

      if (srckey != NULL)
        {
          int invalid = common_safe_int (srckey, &(ret->keys[i]));
          if (invalid)
            {
              free_json_map_int_int (ret);
              if (*err == NULL)
                asprintf (err, "Invalid key '%s' with type 'int': %s",
                          srckey, strerror (-invalid));
              return NULL;
            }
        }

      if (srcval != NULL)
        {
          int invalid;
          if (!YAJL_IS_NUMBER (srcval))
            {
              free_json_map_int_int (ret);
              if (*err == NULL)
                asprintf (err, "Invalid value with type 'int' for key '%s'",
                          srckey);
              return NULL;
            }
          invalid = common_safe_int (YAJL_GET_NUMBER (srcval), &(ret->values[i]));
          if (invalid)
            {
              free_json_map_int_int (ret);
              if (*err == NULL)
                asprintf (err, "Invalid value with type 'int' for key '%s': %s",
                          srckey, strerror (-invalid));
              return NULL;
            }
        }
    }
  return ret;
}

int
append_json_map_int_int (json_map_int_int * map, int key, int val)
{
  size_t len;
  int *keys = NULL;
  int *vals = NULL;

  if (map == NULL)
    return -1;

  if ((SIZE_MAX / sizeof (int) - 1) < map->len)
    return -1;

  len = map->len + 1;
  keys = calloc (1, len * sizeof (int));
  if (keys == NULL)
    return -1;
  vals = calloc (1, len * sizeof (int));
  if (vals == NULL)
    {
      free (keys);
      return -1;
    }

  if (map->len)
    {
      (void) memcpy (keys, map->keys, map->len * sizeof (int));
      (void) memcpy (vals, map->values, map->len * sizeof (int));
    }
  free (map->keys);
  map->keys = keys;
  free (map->values);
  map->values = vals;
  map->keys[map->len] = key;
  map->values[map->len] = val;

  map->len++;
  return 0;
}

yajl_gen_status
gen_json_map_int_bool (void *ctx, const json_map_int_bool * map,
		       const struct parser_context *ptx, parser_error * err)
{
  yajl_gen_status stat = yajl_gen_status_ok;
  yajl_gen g = (yajl_gen) ctx;
  size_t len = 0, i = 0;
  if (map != NULL)
    len = map->len;
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 0);
  stat = yajl_gen_map_open ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  for (i = 0; i < len; i++)
    {
      char numstr[MAX_NUM_STR_LEN];
      int nret;
      nret =
	snprintf (numstr, sizeof (numstr), "%lld",
		  (long long int) map->keys[i]);
      if (nret < 0 || (size_t) nret >= sizeof (numstr))
	{
	  if (!*err)
            asprintf (err, "Error to print string");
	  return yajl_gen_in_error_state;
	}
      stat =
	yajl_gen_string ((yajl_gen) g, (const unsigned char *) numstr,
			 strlen (numstr));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
      stat = yajl_gen_bool ((yajl_gen) g, (int) (map->values[i]));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
    }

  stat = yajl_gen_map_close ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 1);
  return yajl_gen_status_ok;
}

void
free_json_map_int_bool (json_map_int_bool * map)
{
  if (map != NULL)
    {
      size_t i;
      for (i = 0; i < map->len; i++)
	{
	  // No need to free key for type int
	  // No need to free value for type bool
	}
      free (map->keys);
      map->keys = NULL;
      free (map->values);
      map->values = NULL;
      free (map);
    }
}

json_map_int_bool *
make_json_map_int_bool (yajl_val src, const struct parser_context *ctx,
			parser_error * err)
{
  json_map_int_bool *ret = NULL;
  size_t i;
  size_t len;

  (void) ctx;			/* Silence compiler warning.  */

  if (src == NULL || YAJL_GET_OBJECT (src) == NULL)
    return NULL;

  len = YAJL_GET_OBJECT_NO_CHECK (src)->len;
  ret = calloc (1, sizeof (*ret));
  if (ret == NULL)
    return NULL;
  ret->len = 0;
  ret->keys = calloc (len + 1, sizeof (int));
  if (ret->keys == NULL)
    {
      free (ret);
      return NULL;
    }
  ret->values = calloc (len + 1, sizeof (bool));
  if (ret->values == NULL)
    {
      free (ret->keys);
      free (ret);
      return NULL;
    }
  for (i = 0; i < len; i++)
    {
      const char *srckey = YAJL_GET_OBJECT_NO_CHECK (src)->keys[i];
      yajl_val srcval = YAJL_GET_OBJECT_NO_CHECK (src)->values[i];

      ret->keys[i] = 0;
      ret->values[i] = false;
      ret->len = i + 1;

      if (srckey != NULL)
        {
          int invalid = common_safe_int (srckey, &(ret->keys[i]));
          if (invalid)
            {
              free_json_map_int_bool (ret);
              if (*err == NULL)
                asprintf (err, "Invalid key '%s' with type 'int': %s",
                          srckey, strerror (-invalid));
              return NULL;
            }
        }

      if (srcval != NULL)
        {
          if (YAJL_IS_TRUE (srcval))
            ret->values[i] = true;
          else if (YAJL_IS_FALSE (srcval))
            ret->values[i] = false;
          else
            {
              free_json_map_int_bool (ret);
              if (*err == NULL)
                asprintf (err, "Invalid value with type 'bool' for key '%s'",
                          srckey);
              return NULL;
            }
        }
    }
  return ret;
}

int
append_json_map_int_bool (json_map_int_bool * map, int key, bool val)
{
  size_t len;
  int *keys = NULL;
  bool *vals = NULL;

  if (map == NULL)
    return -1;

  if ((SIZE_MAX / sizeof (int) - 1) < map->len
      || (SIZE_MAX / sizeof (bool) - 1) < map->len)
    return -1;

  len = map->len + 1;
  keys = calloc (len, sizeof (int));
  if (keys == NULL)
    return -1;
  vals = calloc (len, sizeof (bool));
  if (vals == NULL)
    {
      free (keys);
      return -1;
    }

  if (map->len)
    {
      (void) memcpy (keys, map->keys, map->len * sizeof (int));
      (void) memcpy (vals, map->values, map->len * sizeof (bool));
    }
  free (map->keys);
  map->keys = keys;
  free (map->values);
  map->values = vals;
  map->keys[map->len] = key;
  map->values[map->len] = val;

  map->len++;
  return 0;
}

yajl_gen_status
gen_json_map_int_string (void *ctx, const json_map_int_string * map,
			 const struct parser_context *ptx, parser_error * err)
{
  yajl_gen_status stat = yajl_gen_status_ok;
  yajl_gen g = (yajl_gen) ctx;
  size_t len = 0, i = 0;
  if (map != NULL)
    len = map->len;
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 0);

  stat = yajl_gen_map_open ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  for (i = 0; i < len; i++)
    {
      char numstr[MAX_NUM_STR_LEN];
      int nret;
      nret =
	snprintf (numstr, sizeof (numstr), "%lld",
		  (long long int) map->keys[i]);
      if (nret < 0 || (size_t) nret >= sizeof (numstr))
	{
	  if (!*err)
            asprintf (err, "Error to print string");
	  return yajl_gen_in_error_state;
	}
      stat =
	yajl_gen_string ((yajl_gen) g, (const unsigned char *) numstr,
			 strlen (numstr));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
      stat =
	yajl_gen_string ((yajl_gen) g,
			 (const unsigned char *) (map->values[i]),
			 strlen (map->values[i]));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
    }

  stat = yajl_gen_map_close ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 1);
  return yajl_gen_status_ok;
}

void
free_json_map_int_string (json_map_int_string * map)
{
  if (map != NULL)
    {
      size_t i;
      for (i = 0; i < map->len; i++)
	{
	  // No need to free key for type int
	  free (map->values[i]);
	  map->values[i] = NULL;
	}
      free (map->keys);
      map->keys = NULL;
      free (map->values);
      map->values = NULL;
      free (map);
    }
}

json_map_int_string *
make_json_map_int_string (yajl_val src, const struct parser_context *ctx,
			  parser_error * err)
{
  size_t i;
  size_t len;
  json_map_int_string *ret = NULL;

  if (src == NULL || YAJL_GET_OBJECT (src) == NULL)
    return NULL;

  (void) ctx;			/* Silence compiler warning.  */

  len = YAJL_GET_OBJECT_NO_CHECK (src)->len;

  ret = calloc (1, sizeof (*ret));
  if (ret == NULL)
    return NULL;

  ret->len = 0;
  ret->keys = calloc (len + 1, sizeof (int));
  if (ret->keys == NULL)
    {
      free (ret);
      return NULL;
    }

  ret->values = calloc (len + 1, sizeof (char *));
  if (ret->values == NULL)
    {
      free (ret->keys);
      free (ret);
      return NULL;
    }

  for (i = 0; i < len; i++)
    {
      const char *srckey = YAJL_GET_OBJECT_NO_CHECK (src)->keys[i];
      yajl_val srcval = YAJL_GET_OBJECT_NO_CHECK (src)->values[i];

      ret->keys[i] = 0;
      ret->values[i] = NULL;
      ret->len = i + 1;

      if (srckey != NULL)
        {
          int invalid;
          invalid = common_safe_int (srckey, &(ret->keys[i]));
          if (invalid)
            {
              free_json_map_int_string (ret);
              if (*err == NULL)
                asprintf (err, "Invalid key '%s' with type 'int': %s",
                          srckey, strerror (-invalid));
              return NULL;
            }
        }

      if (srcval != NULL)
        {
          if (!YAJL_IS_STRING (srcval))
            {
              free_json_map_int_string (ret);
              if (*err == NULL)
                asprintf (err, "Invalid value with type 'string' for key '%s'",
                          srckey);
              return NULL;
            }
          char *str = YAJL_GET_STRING_NO_CHECK (srcval);
          ret->values[i] = strdup (str ? str : "");
        }
    }
  return ret;
}

int
append_json_map_int_string (json_map_int_string * map, int key,
			    const char *val)
{
  size_t len;
  int *keys = NULL;
  char **vals = NULL;
  char *new_value;

  if (map == NULL)
    return -1;

  if ((SIZE_MAX / sizeof (int) - 1) < map->len
      || (SIZE_MAX / sizeof (char *) - 1) < map->len)
    return -1;

  len = map->len + 1;
  keys = realloc (map->keys, len * sizeof (int));
  if (keys == NULL)
    return -1;
  map->keys = keys;

  vals = realloc (map->values, len * sizeof (char *));
  if (vals == NULL)
    return -1;
  map->values = vals;

  new_value = strdup (val ? val : "");
  if (new_value == NULL)
    return -1;

  map->keys[map->len] = key;
  map->values[map->len] = new_value;

  map->len++;
  return 0;
}

yajl_gen_status
gen_json_map_string_int (void *ctx, const json_map_string_int * map,
			 const struct parser_context *ptx, parser_error * err)
{
  yajl_gen_status stat = yajl_gen_status_ok;
  yajl_gen g = (yajl_gen) ctx;
  size_t len = 0, i = 0;
  if (map != NULL)
    len = map->len;
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 0);
  stat = yajl_gen_map_open ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  for (i = 0; i < len; i++)
    {
      stat =
	yajl_gen_string ((yajl_gen) g, (const unsigned char *) (map->keys[i]),
			 strlen (map->keys[i]));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
      stat = map_int (g, map->values[i]);
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
    }

  stat = yajl_gen_map_close ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 1);
  return yajl_gen_status_ok;
}

void
free_json_map_string_int (json_map_string_int * map)
{
  if (map != NULL)
    {
      size_t i;
      for (i = 0; i < map->len; i++)
	{
	  free (map->keys[i]);
	  map->keys[i] = NULL;
	}
      free (map->keys);
      map->keys = NULL;
      free (map->values);
      map->values = NULL;
      free (map);
    }
}

json_map_string_int *
make_json_map_string_int (yajl_val src, const struct parser_context *ctx,
			  parser_error * err)
{
  json_map_string_int *ret = NULL;
  size_t i;
  size_t len;

  (void) ctx;			/* Silence compiler warning.  */

  if (src == NULL || YAJL_GET_OBJECT (src) == NULL)
    return NULL;

  len = YAJL_GET_OBJECT_NO_CHECK (src)->len;
  ret = calloc (1, sizeof (*ret));
  if (ret == NULL)
    {
      *(err) = strdup ("error allocating memory");
      return NULL;
    }
  ret->len = 0;
  ret->keys = calloc (len + 1, sizeof (char *));
  if (ret->keys == NULL)
    {
      free (ret);
      *(err) = strdup ("error allocating memory");
      return NULL;
    }
  ret->values = calloc (len + 1, sizeof (int));
  if (ret->values == NULL)
    {
      free (ret->keys);
      free (ret);
      *(err) = strdup ("error allocating memory");
      return NULL;
    }
  for (i = 0; i < len; i++)
    {
      const char *srckey = YAJL_GET_OBJECT_NO_CHECK (src)->keys[i];
      yajl_val srcval = YAJL_GET_OBJECT_NO_CHECK (src)->values[i];

      ret->keys[i] = NULL;
      ret->values[i] = 0;
      ret->len = i + 1;

      ret->keys[i] = strdup (srckey ? srckey : "");
      if (ret->keys[i] == NULL)
        {
          free_json_map_string_int (ret);
          *(err) = strdup ("error allocating memory");
          return NULL;
        }

      if (srcval != NULL)
        {
          int invalid;
          if (!YAJL_IS_NUMBER (srcval))
            {
              free_json_map_string_int (ret);
              if (*err == NULL)
                asprintf (err, "Invalid value with type 'int' for key '%s'",
                          srckey);
              return NULL;
            }
          invalid = common_safe_int (YAJL_GET_NUMBER (srcval), &(ret->values[i]));
          if (invalid)
            {
              free_json_map_string_int (ret);
              if (*err == NULL)
                asprintf (err, "Invalid value with type 'int' for key '%s': %s",
                          srckey, strerror (-invalid));
              return NULL;
            }
        }
    }
  return ret;
}

int
append_json_map_string_int (json_map_string_int * map, const char *key,
			    int val)
{
  size_t len;
  char **keys = NULL;
  int *vals = NULL;
  char *new_value;

  if (map == NULL)
    return -1;

  if ((SIZE_MAX / sizeof (char *) - 1) < map->len
      || (SIZE_MAX / sizeof (int) - 1) < map->len)
    return -1;

  len = map->len + 1;
  keys = realloc (map->keys, len * sizeof (char *));
  if (keys == NULL)
    return -1;
  map->keys = keys;
  vals = realloc (map->values, len * sizeof (int));
  if (vals == NULL)
    return -1;
  map->values = vals;

  new_value = strdup (key ? key : "");
  if (new_value == NULL)
    return -1;
  map->keys[map->len] = new_value;
  map->values[map->len] = val;

  map->len++;
  return 0;
}

yajl_gen_status
gen_json_map_string_bool (void *ctx, const json_map_string_bool * map,
			  const struct parser_context *ptx,
			  parser_error * err)
{
  yajl_gen_status stat = yajl_gen_status_ok;
  yajl_gen g = (yajl_gen) ctx;
  size_t len = 0, i = 0;
  if (map != NULL)
    len = map->len;
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 0);
  stat = yajl_gen_map_open ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  for (i = 0; i < len; i++)
    {
      stat =
	yajl_gen_string ((yajl_gen) g, (const unsigned char *) (map->keys[i]),
			 strlen (map->keys[i]));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
      stat = yajl_gen_bool ((yajl_gen) g, (int) (map->values[i]));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
    }

  stat = yajl_gen_map_close ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 1);
  return yajl_gen_status_ok;
}

void
free_json_map_string_bool (json_map_string_bool * map)
{
  if (map != NULL)
    {
      size_t i;
      for (i = 0; i < map->len; i++)
	{
	  free (map->keys[i]);
	  map->keys[i] = NULL;
	  // No need to free value for type bool
	}
      free (map->keys);
      map->keys = NULL;
      free (map->values);
      map->values = NULL;
      free (map);
    }
}

json_map_string_bool *
make_json_map_string_bool (yajl_val src, const struct parser_context *ctx,
			   parser_error * err)
{
  json_map_string_bool *ret = NULL;
  size_t i;
  size_t len;

  (void) ctx;			/* Silence compiler warning.  */

  len = YAJL_GET_OBJECT_NO_CHECK (src)->len;

  if (src == NULL || YAJL_GET_OBJECT (src) == NULL)
    return NULL;

  ret = calloc (1, sizeof (*ret));
  if (ret == NULL)
    return NULL;
  ret->len = 0;
  ret->keys = calloc (len + 1, sizeof (char *));
  if (ret->keys == NULL)
    {
      free (ret);
      return NULL;
    }

  ret->values = calloc (len + 1, sizeof (bool));
  if (ret->values == NULL)
    {
      free (ret->values);
      free (ret);
      return NULL;
    }
  for (i = 0; i < len; i++)
    {
      const char *srckey = YAJL_GET_OBJECT_NO_CHECK (src)->keys[i];
      yajl_val srcval = YAJL_GET_OBJECT_NO_CHECK (src)->values[i];

      ret->keys[i] = NULL;
      ret->values[i] = NULL;
      ret->len = i + 1;

      ret->keys[i] = strdup (srckey ? srckey : "");
      if (ret->keys[i] == NULL)
        {
          free_json_map_string_bool (ret);
          *(err) = strdup ("error allocating memory");
          return NULL;
        }
      if (srcval != NULL)
        {
          if (YAJL_IS_TRUE (srcval))
            ret->values[i] = true;
          else if (YAJL_IS_FALSE (srcval))
            ret->values[i] = false;
          else
            {
              free_json_map_string_bool (ret);
              if (*err == NULL)
                asprintf (err, "Invalid value with type 'bool' for key '%s'",
                          srckey);
              return NULL;
            }
        }
    }
  return ret;
}

int
append_json_map_string_bool (json_map_string_bool * map, const char *key,
			     bool val)
{
  size_t len;
  char **keys = NULL;
  bool *vals = NULL;
  char *new_value;

  if (map == NULL)
    return -1;

  if ((SIZE_MAX / sizeof (char *) - 1) < map->len
      || (SIZE_MAX / sizeof (bool) - 1) < map->len)
    return -1;

  len = map->len + 1;
  keys = calloc (len, sizeof (char *));
  if (keys == NULL)
    return -1;
  vals = calloc (len, sizeof (bool));
  if (vals == NULL)
    {
      free (keys);
      return -1;
    }

  new_value = strdup (key ? key : "");
  if (new_value == NULL)
    {
      free (vals);
      free (keys);
      return -1;
    }

  if (map->len)
    {
      (void) memcpy (keys, map->keys, map->len * sizeof (char *));
      (void) memcpy (vals, map->values, map->len * sizeof (bool));
    }
  free (map->keys);
  map->keys = keys;
  free (map->values);
  map->values = vals;
  map->keys[map->len] = new_value;
  map->values[map->len] = val;

  map->len++;
  return 0;
}

yajl_gen_status
gen_json_map_string_string (void *ctx, const json_map_string_string * map,
			    const struct parser_context *ptx,
			    parser_error * err)
{
  yajl_gen_status stat = yajl_gen_status_ok;
  yajl_gen g = (yajl_gen) ctx;
  size_t len = 0, i = 0;
  if (map != NULL)
    len = map->len;

  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 0);

  stat = yajl_gen_map_open ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);

  for (i = 0; i < len; i++)
    {
      stat =
	yajl_gen_string ((yajl_gen) g, (const unsigned char *) (map->keys[i]),
			 strlen (map->keys[i]));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
      stat =
	yajl_gen_string ((yajl_gen) g,
			 (const unsigned char *) (map->values[i]),
			 strlen (map->values[i]));
      if (yajl_gen_status_ok != stat)
	GEN_SET_ERROR_AND_RETURN (stat, err);
    }

  stat = yajl_gen_map_close ((yajl_gen) g);
  if (yajl_gen_status_ok != stat)
    GEN_SET_ERROR_AND_RETURN (stat, err);
  if (!len && !(ptx->options & OPT_GEN_SIMPLIFY))
    yajl_gen_config (g, yajl_gen_beautify, 1);
  return yajl_gen_status_ok;
}

void
free_json_map_string_string (json_map_string_string * map)
{
  if (map != NULL)
    {
      size_t i;
      for (i = 0; i < map->len; i++)
	{
	  free (map->keys[i]);
	  map->keys[i] = NULL;
	  free (map->values[i]);
	  map->values[i] = NULL;
	}
      free (map->keys);
      map->keys = NULL;
      free (map->values);
      map->values = NULL;
      free (map);
    }
}

json_map_string_string *
make_json_map_string_string (yajl_val src, const struct parser_context *ctx,
			     parser_error * err)
{
  json_map_string_string *ret = NULL;
  size_t i;
  size_t len;

  (void) ctx;			/* Silence compiler warning.  */
  if (src == NULL || YAJL_GET_OBJECT (src) == NULL)
    return NULL;

  len = YAJL_GET_OBJECT_NO_CHECK (src)->len;

  ret = malloc (sizeof (*ret));
  if (ret == NULL)
    {
      *(err) = strdup ("error allocating memory");
      return NULL;
    }

  ret->len = 0;

  ret->keys = calloc (len + 1, sizeof (char *));
  if (ret->keys == NULL)
    {
      free (ret);
      *(err) = strdup ("error allocating memory");
      return NULL;
    }

  ret->values = calloc (len + 1, sizeof (char *));
  if (ret->values == NULL)
    {
      free (ret->keys);
      free (ret);
      *(err) = strdup ("error allocating memory");
      return NULL;
    }
  for (i = 0; i < len; i++)
    {
      const char *srckey = YAJL_GET_OBJECT_NO_CHECK (src)->keys[i];
      yajl_val srcval = YAJL_GET_OBJECT_NO_CHECK (src)->values[i];

      ret->keys[i] = NULL;
      ret->values[i] = NULL;
      ret->len = i + 1;

      ret->keys[i] = strdup (srckey ? srckey : "");
      if (ret->keys[i] == NULL)
        {
          free_json_map_string_string (ret);
          return NULL;
        }
      if (srcval != NULL)
        {
          char *str;
          if (!YAJL_IS_STRING (srcval))
            {
              free_json_map_string_string (ret);
              if (*err == NULL)
                asprintf (err, "Invalid value with type 'string' for key '%s'",
                          srckey);
              return NULL;
            }

          str = YAJL_GET_STRING_NO_CHECK (srcval);

          ret->values[i] = strdup (str ? str : "");
          if (ret->values[i] == NULL)
            {
              free_json_map_string_string (ret);
              return NULL;
            }
        }
    }
  return ret;
}

int
append_json_map_string_string (json_map_string_string * map, const char *key,
			       const char *val)
{
  size_t len, i;
  char **keys = NULL;
  char **values = NULL;
  char *new_key = NULL;
  char *new_value = NULL;

  if (map == NULL)
    return -1;

  for (i = 0; i < map->len; i++)
    {
      if (strcmp (map->keys[i], key) == 0)
	{
          char *v = strdup (val ? val : "");
          if (v == NULL)
            return -1;
	  free (map->values[i]);
	  map->values[i] = v;
	  return 0;
	}
    }

  if ((SIZE_MAX / sizeof (char *) - 1) < map->len)
    return -1;

  new_key = strdup (key ? key : "");
  if (new_key == NULL)
    goto cleanup;

  new_value = strdup (val ? val : "");
  if (new_value == NULL)
    goto cleanup;

  len = map->len + 1;
  keys = realloc (map->keys, len * sizeof (char *));
  if (keys == NULL)
    goto cleanup;
  map->keys = keys;
  map->keys[map->len] = NULL;

  values = realloc (map->values, len * sizeof (char *));
  if (values == NULL)
    goto cleanup;

  map->keys[map->len] = new_key;
  map->values = values;
  map->values[map->len] = new_value;

  map->len++;
  return 0;

 cleanup:
  free (new_value);
  free (new_key);
  return -1;
}

char *
json_marshal_string (const char *str, size_t length,
		     const struct parser_context *ctx, parser_error * err)
{
  yajl_gen g = NULL;
  struct parser_context tmp_ctx = { 0 };
  const unsigned char *gen_buf = NULL;
  char *json_buf = NULL;
  size_t gen_len = 0;
  yajl_gen_status stat;

  if (str == NULL || err == NULL)
    return NULL;

  *err = NULL;
  if (ctx == NULL)
    ctx = (const struct parser_context *) (&tmp_ctx);

  if (!json_gen_init (&g, ctx))
    {
      *err = strdup ("Json_gen init failed");
      goto out;
    }
  stat = yajl_gen_string ((yajl_gen) g, (const unsigned char *) str, length);
  if (yajl_gen_status_ok != stat)
    {
      asprintf (err, "error generating json, errcode: %d", (int) stat);
      goto free_out;
    }
  yajl_gen_get_buf (g, &gen_buf, &gen_len);
  if (gen_buf == NULL)
    {
      *err = strdup ("Error to get generated json");
      goto free_out;
    }

  json_buf = calloc (1, gen_len + 1);
  if (json_buf == NULL)
    {
      *err = strdup ("error allocating memory");
      goto free_out;
    }

  (void) memcpy (json_buf, gen_buf, gen_len);
  json_buf[gen_len] = '\\0';

free_out:
  yajl_gen_clear (g);
  yajl_gen_free (g);
out:
  return json_buf;
}
        """)
        fcntl.flock(source_file, fcntl.LOCK_UN)
