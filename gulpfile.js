'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass')(require('sass'));

function buildStyles() {
  return gulp.src('scss/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('css'));
};

exports.buildStyles = buildStyles;
exports.watch = function () {
  gulp.watch('scss/**/*.scss', buildStyles);
};