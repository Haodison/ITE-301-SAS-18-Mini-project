package com.android.moviecinema;
import android.content.Context;
import android.content.DialogInterface;
import android.support.v7.app.AlertDialog;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;
public class OnLongClickListenerMovieRecord implements View.OnLongClickListener {
Context context;
String id;
@Override
public boolean onLongClick(View view) {
context = view.getContext();
id = view.getTag().toString();
final CharSequence[] items = { "Edit", "Delete" };
new AlertDialog.Builder(context).setTitle("Movie Record")
.setItems(items, new DialogInterface.OnClickListener() {
public void onClick(DialogInterface dialog, int item) {
if (item == 0) {
editRecord(Integer.parseInt(id));
}else if (item == 1) {
boolean deleteSuccessful = new
TableControllerMovie(context).delete(Integer.parseInt(id));
if (deleteSuccessful){
Toast.makeText(context, "Movie record was deleted.",
Toast.LENGTH_SHORT).show();
}else{
Toast.makeText(context, "Error deleting movie record.",
Toast.LENGTH_SHORT).show();
}
((MainActivity) context).countRecords();
((MainActivity) context).readRecords();

}
dialog.dismiss();
}
}).show();
return false;
}
public void editRecord(final int movieId) {
final TableControllerMovie tableControllerMovie = new
TableControllerMovie(context);
Movie movie = tableControllerMovie.readSingleRecord(movieId);
LayoutInflater inflater = (LayoutInflater)
context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
final View formElementsView = inflater.inflate(R.layout.movie_input_form, null,
false);
final EditText title = (EditText)
formElementsView.findViewById(R.id.editTextTitle);
final EditText genre = (EditText)
formElementsView.findViewById(R.id.editTextGenre);
final EditText director = (EditText)
formElementsView.findViewById(R.id.editTextDirector);
title.setText(movie.title);
genre.setText(movie.genre);
director.setText(movie.director);
new AlertDialog.Builder(context)
.setView(formElementsView)
.setTitle("Edit Movie")

.setPositiveButton("Save Changes",
new DialogInterface.OnClickListener() {
public void onClick(DialogInterface dialog, int id) {
Movie movie = new Movie();
movie.id = movieId;
movie.title= title.getText().toString();
movie.genre = genre.getText().toString();
movie.director = director.getText().toString();

boolean updateSuccessful =
tableControllerMovie.update(movie);
if(updateSuccessful){
Toast.makeText(context, "Movie record was updated.",
Toast.LENGTH_SHORT).show();
}else{
Toast.makeText(context, "Error updating movie
record.", Toast.LENGTH_SHORT).show();
}

MainActivity.getInstance().countRecords();
MainActivity.getInstance().readRecords();
}
}).show();
}
}
