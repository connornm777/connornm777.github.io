\documentclass[10pt, mathserif, structurebold]{beamer}
\usecolortheme{beaver}
\usetheme{AnnArbor}
\usepackage{hyperref}
\usepackage{cancel}
\usepackage{mathtools}
\usepackage{graphics}
\usepackage{animate}
\usepackage{multimedia}
\usepackage{amsmath}
\title[]{Riemann Curvature Tensor}
\author{Connor}
\date{}
\begin{document}

\frame{\titlepage}



%##############################################################################################################
\begin{frame}

\begin{itemize}
\item
In flat space, each point can be identified with a position vector
\item
The position of a point given a position vector from another point is then just their sum
\item 
In curved space, we cannot identify points in space with position vectors 
\item
However, each point in space can be treated as flat locally, so that only neighboring points (defined as those only some infinitesimal distance away)
can be indicated with a position vector originating from center point of the neighborhood
\end{itemize}

\end{frame}


%##############################################################################################################
\begin{frame}

\begin{itemize}
\item
The vector $\delta \vec{u}$ points from point $A$ to neighboring point $B$
\item
The vector $\delta \vec{w}$ points from point $A$ to neighboring point $C$
\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[scale=0.7]{pics/abc.png}
\end{figure}

\end{frame}


%##############################################################################################################
\begin{frame}

\begin{itemize}
\item 
Vector $\delta \vec{u}$ at point $C$, locates the neighboring point $D$
\item
Vector $\delta \vec{w}$ at point $B$, locates the neighboring point $E$
\item 
$E$ close to $B$, $D$ close to $C$, $B$ and $C$ close to $A$
\item
$E$ and $D$ NOT close to $A$, cannot uniquely identify with a position vector from $A$ to $E$ and $D$
\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[scale=0.7]{pics/abcde.png}
\end{figure}

\end{frame}

%##############################################################################################################
\begin{frame}

\begin{itemize}
\item
$\delta\vec{w}$ and $\delta\vec{u}$ are treated as close enough to be locally flat and indicate positions around $A$
\item 
Their sum $\delta\vec{w}+\delta\vec{u}$ is long enough to need corrections, and does not uniquely identify a point in space
\item
In general for curved space, the points $D$ and $E$ do not coincide
\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[scale=0.7]{pics/abcde.png}
\end{figure}

\end{frame}


%##############################################################################################################
\begin{frame}

\begin{itemize}
\item
Instead of adding vectors like we would in flat space, we may parallel transport $\delta\vec{w}$ along $\delta\vec{u}$  resulting in 
the vector $\delta \vec{w}^{\prime}$ at point $B$ and vice versa for $\delta\vec{u}^{\prime}$ at point $C$.
\item 
This compensates for the curvature of space and identifies a unique point in space $F$ independent of order IF 
space is torsionless
\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[scale=0.7]{pics/abcdef.png}
\end{figure}

\end{frame}


%##############################################################################################################
\begin{frame}

\begin{itemize}
\item
If there is torsion, even $\delta\vec{u}^{\prime}$ and $\delta\vec{w}^{\prime}$ do not coincide to the same point
\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[scale=0.7]{pics/abcdegh.png}
\end{figure}

\end{frame}


%##############################################################################################################
\begin{frame}

\begin{itemize}
\item
For infinitesimal vectors, we only require the lowest order correction of parallel transport, the gradient of the vector
\end{itemize}

\begin{equation*}
\begin{split}
\delta\vec{u}^{\prime}&=\delta\vec{u}+\nabla_{{\delta\vec{w}}}\delta\vec{u}\\
\delta\vec{w}^{\prime}&=\delta\vec{w}+\nabla_{{\delta\vec{u}}}\delta\vec{w}\\
\end{split}
\end{equation*}

\begin{figure}[H]
\centering
\includegraphics[scale=0.7]{pics/abcf.png}
\end{figure}

\end{frame}


%##############################################################################################################
\begin{frame}

\begin{itemize}
\item
These two paths correspond to the same point $F$, they do NOT correspond to the same tangent space AT $F$. 
\item
We can transport another vector $\vec{v}$ on the path $ABF$, and the path $ACF$ and compare the difference at point $F$
\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[scale=0.7]{pics/abcfdv.png}
\end{figure}

\end{frame}

%##############################################################################################################
\begin{frame}

\begin{equation*}
\begin{split}
\vec{v}_{AC}&=\vec{v}+\nabla_{\delta \vec{w}}\vec{v}\\
\vec{v}_{ACF}&=\vec{v}_{AC}+\nabla_{\delta \vec{u}^{\prime}}\vec{v}_{AC}\\
\vec{v}_{AB}&=\vec{v}+\nabla_{\delta \vec{u}}\vec{v}\\
\vec{v}_{ABF}&=\vec{v}_{AB}+\nabla_{\delta \vec{w}^{\prime}}\vec{v}_{AB}\\
\implies\delta\vec{v}&=\vec{v}_{ABF}-\vec{v}_{ACF}\\
&=\left(1+\nabla_{\delta\vec{w}^{\prime}}\right)\vec{v}_{AB}
-\left(1+\nabla_{\delta\vec{u}^{\prime}}\right)\vec{v}_{AC}\\
&=\left(1+\nabla_{\delta\vec{w}^{\prime}}\right)\left(1+\nabla_{\delta\vec{u}}\right)\vec{v}
-\left(1+\nabla_{\delta\vec{u}^{\prime}}\right)\left(1+\nabla_{\delta\vec{w}}\right)\vec{v}\\
\implies\delta\vec{v}&=\left[
\left(1+\nabla_{\delta\vec{w}^{\prime}}\right)\left(1+\nabla_{\delta\vec{u}}\right)
-\left(1+\nabla_{\delta\vec{u}^{\prime}}\right)\left(1+\nabla_{\delta\vec{w}}\right)
\right]\vec{v}\\
\end{split}
\end{equation*}

The Riemann tensor is defined as:

\begin{equation}
\delta \vec{v}=R(\delta \vec{w}, \delta \vec{u})\vec{v}
\end{equation}


\end{frame}


%##############################################################################################################
\begin{frame}


Riemann tensor largest terms are second order in size of the infinitesimal transport vectors.
\begin{equation*}
\begin{split}
\implies R(\delta \vec{w}, \delta \vec{u})&=\left(1+\nabla_{\delta\vec{w}^{\prime}}\right)\left(1+\nabla_{\delta\vec{u}}\right)
-\left(1+\nabla_{\delta\vec{u}^{\prime}}\right)\left(1+\nabla_{\delta\vec{w}}\right)\\
%
&=\left(1+\nabla_{\delta\vec{w}+\nabla_{\delta\vec{u}}\delta\vec{w}}\right)\left(1+\nabla_{\delta\vec{u}}\right)
-\left(1+\nabla_{\delta\vec{u}+\nabla_{\delta\vec{w}}\delta\vec{u}}\right)\left(1+\nabla_{\delta\vec{w}}\right)\\
%
\nabla_{\vec{a}+\vec{b}}&=\nabla_{\vec{a}}+\nabla_{\vec{b}} \\
%
\implies R(\delta\vec{w}, \delta\vec{u})&=
\left(1+\nabla_{\delta\vec{w}}+\nabla_{\nabla_{\delta\vec{u}}\delta\vec{w}}\right)\left(1+\nabla_{\delta\vec{u}}\right)\\
&-\left(1+\nabla_{\delta\vec{u}}+\nabla_{\nabla_{\delta\vec{w}}\delta\vec{u}}\right)\left(1+\nabla_{\delta\vec{w}}\right)\\
%
&=\nabla_{\delta\vec{w}}\nabla_{\delta\vec{u}}-\nabla_{\delta\vec{u}}\nabla_{\delta\vec{w}}
+\nabla_{\nabla_{\delta \vec{u}}\delta\vec{w}}-\nabla_{\nabla_{\delta\vec{w}}\delta\vec{u}} + O(\delta^3)\\
%
&=\nabla_{\delta\vec{w}}\nabla_{\delta\vec{u}}-\nabla_{\delta\vec{u}}\nabla_{\delta\vec{w}}
+\nabla_{\nabla_{\delta \vec{u}}\delta\vec{w}}-\nabla_{\nabla_{\delta\vec{w}}\delta\vec{u}}\\
%
&=\nabla_{\delta\vec{w}}\nabla_{\delta\vec{u}}-\nabla_{\delta\vec{u}}\nabla_{\delta\vec{w}}
-\nabla_{\left(\nabla_{\delta\vec{w}}\delta\vec{u}-\nabla_{\delta\vec{u}}\delta\vec{w}\right)}\\
%
\end{split}
\end{equation*}


\end{frame}


%##############################################################################################################
\begin{frame}


\begin{equation*}
\implies R(\delta\vec{w}, \delta{u})=\nabla_{\delta\vec{w}}\nabla_{\delta\vec{u}}-\nabla_{\delta\vec{u}}\nabla_{\delta\vec{w}}
-\nabla_{\left(\nabla_{\delta\vec{w}}\delta\vec{u}-\nabla_{\delta\vec{u}}\delta\vec{w}\right)}
\end{equation*}

Definition of Lie bracket of two vectors also results in a vector (I don't like using a commutator here, you aren't multiplying
the vectors, this isn't a two form $[\vec{a}, \vec{b}]=2 \vec{a} \wedge \vec{b}$):

\begin{equation*}
\vec{\mathcal{L}}(\vec{a}, \vec{b})=\nabla_{\vec{a}}\vec{b}-\nabla_{\vec{b}}\vec{a}
\end{equation*}


\begin{equation*}
\implies \boxed{R(\delta\vec{w}, \delta\vec{u})
=\left[\nabla_{\delta\vec{w}}, \nabla_{\delta\vec{u}}\right]
-\nabla_{\vec{\mathcal{L}}(\delta \vec{w}, \delta \vec{u})}}
\end{equation*}



\end{frame}


%##############################################################################################################
\begin{frame}

\begin{equation*}
R(\delta\vec{w}, \delta\vec{u})
=\left[\nabla_{\delta\vec{w}}, \nabla_{\delta\vec{u}}\right]
-\nabla_{\vec{\mathcal{L}}(\delta \vec{w}, \delta \vec{u})}
\end{equation*}


\begin{equation*}
\delta \vec{v} = R(\delta \vec{w}, \delta \vec{u}) \vec{v}
\end{equation*}

\begin{figure}[H]
\centering
\includegraphics[scale=0.7]{pics/abcfdv.png}
\end{figure}

\end{frame}



\end{document}
