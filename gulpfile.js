'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass')(require('sass'));

function buildStyles() {
  return gulp.src('src/static/scss/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('src/static/css'));
};

exports.buildStyles = buildStyles;
exports.watch = function () {
  gulp.watch('src/static/scss/**/*.scss', buildStyles);
};