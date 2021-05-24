import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { MatButtonModule } from  '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card'
import { HttpClientModule } from  '@angular/common/http';
import { MatSnackBarModule } from  '@angular/material/snack-bar';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './components/user/login/login.component';
import { SimpleHeaderComponent } from './components/template/simple-header/simple-header.component';
import { CreateComponent } from './components/user/create/create.component';
import { ConsultaReadComponent } from './components/consulta/consulta-read/consulta-read.component';
import { MatTableModule } from '@angular/material/table';
import { MatSelectModule } from '@angular/material/select';
import { MatDialogModule } from '@angular/material/dialog';

import { ConsultaCreateComponent } from './components/consulta/consulta-create/consulta-create.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SimpleHeaderComponent,
    CreateComponent,
    ConsultaReadComponent,
    ConsultaCreateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    FormsModule,
    MatButtonModule,
    MatIconModule,
    MatCardModule,
    MatTableModule,
    HttpClientModule,
    MatSnackBarModule,
    MatSelectModule,
    MatDialogModule
  ],
  providers: [
    
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
