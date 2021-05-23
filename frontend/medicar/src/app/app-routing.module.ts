import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuardService as AuthGuard} from './auth/auth-guard.service';
import { ConsultaReadComponent } from './components/consulta/consulta-read/consulta-read.component';
import { CreateComponent } from './components/user/create/create.component';
import { LoginComponent } from './components/user/login/login.component';

const routes: Routes = [
  {
    path:"login",
    component: LoginComponent
  },
  {
    path:"registrar",
    component: CreateComponent
  },
  {
    path:"consultas",
    component: ConsultaReadComponent,
    canActivate: [AuthGuard]
  },
  
  { path: "", redirectTo: "login", pathMatch:"full"}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
